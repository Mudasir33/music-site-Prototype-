
import os
from socket import if_indextoname
import uuid as uuid
from flask import Flask, make_response, send_from_directory, url_for, render_template, request, redirect, abort
from flask.helpers import flash
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename
from db.index import db # där db är databas objektet från index.py
app = Flask(__name__, static_folder="web/static", static_url_path="", template_folder="web/template")
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024

UPLOAD_FOLDER = 'web/static/img'
app.config['UPLOAD_PATH'] = UPLOAD_FOLDER

UPLOAD_FOLD = 'web/static/music'
app.config['UPLOAD_PAT'] = UPLOAD_FOLD

UPLOAD_FOL = 'web/static/thumb'
app.config['UPLOAD_PA'] = UPLOAD_FOL


# Klienten kan skicka in ett namn som sparas i databasen





def user(username,password):
    people = db.child("konto").get()
    for person in people.each():
        check_name = person.val().get("username")
        check_password = person.val().get("password")
       
    
        if check_name != None  and check_password != None:
            if username == check_name and password == check_password:
                print(person)
                return person
    
    




@app.route("/")
def site():
    
    return render_template("logain.html")

@app.route('/start_sida', methods=["POST"], )
def site_post():
    
    uploaded_file = request.files['file']
 
    filename = secure_filename(uploaded_file.filename)
    
    file_name = str(uuid.uuid1()) + "_" + filename

    saver = request.files["file"]

    uploaded_file=file_name
    
    saver.save(os.path.join(app.config['UPLOAD_PATH'], filename))


    user = request.form.get("username") 
    password = request.form.get("password")
    email = request.form.get("email")
    password1 = request.form.get("password1")
    
    if password != password1:
        return redirect ("/")
    if password == password1:
        account = {"username": user,  "email":email, "password":password, "admin":"false", "file":filename, "music":None}
        
        db.child("konto").push(account)
        return redirect("/sign_in")
   


@app.route("/sign_in")
def sign():
    return render_template("sign_in.html")




@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        people = db.child("konto").get()
       
        person = user(username, password)

        if person == None:
            return redirect ("/login") 
       
        

        check_admin = person.val().get("admin")
        email = person.val().get("email")
        file = person.val().get("file")
        musik = person.val().get("music")

        if check_admin == "false":
            
            resp = make_response(render_template('profil.html', user=username, pas = password, email = email, file=file, musik=musik))
            resp.set_cookie("username",username)
            resp.set_cookie("password", password)
            
        
            return resp
        if check_admin.lower() == "true":
            namelist = []
            passlist =[]
            elist=[]
            people = db.child("konto").get()
            for person in people.each():
                username = person.val()["username"]
                password = person.val()["password"]
                email = person.val()["email"]
                namelist.append(username)
                passlist.append(password)
                elist.append(email)
                print(username)
                print(password)
            return render_template("admin.html", pas = password, passes = passlist, names=namelist, name= username, email = email, emails= elist)  
    return redirect ("/") 






@app.route('/hem', methods=['GET', 'POST'])
def hem():
    name = request.cookies.get('username')
    password = request.cookies.get('password')
    person = user(name, password)
    file = person.val().get('file')
   
    return render_template("startsida.html", user=name, pas=password, file= file)

@app.route('/profil', methods=['GET', 'POST'])
def profil():
    name = request.cookies.get('username')
    password = request.cookies.get('password')
    person = user(name, password)
    file = person.val().get('file')
    musik = person.val().get("music")
    return render_template("profil2.html", user=name, pas=password, file= file, musik=musik)


@app.route('/album', methods=['GET', 'POST'])
def album():
    name = request.cookies.get('username')
    password = request.cookies.get('password')
    person = user(name, password)
    file = person.val().get('file')

    return render_template("album.html", user=name, pas=password, file= file)


@app.route('/playlist', methods=['GET', 'POST'])
def playlist():
    name = request.cookies.get('username')
    password = request.cookies.get('password')
    person = user(name, password)
    file = person.val().get('file')

    return render_template("playlist.html", user=name, pas=password, file= file) 

@app.route('/repost', methods=['GET', 'POST'])
def repost():
    name = request.cookies.get('username')
    password = request.cookies.get('password')
    person = user(name, password)
    file = person.val().get('file')

    return render_template("repost.html", user=name, pas=password, file= file) 


@app.route ("/upload", methods= ["GET","POST"])
def upploaded():
    name = request.cookies.get('username')
    password = request.cookies.get('password')
    person = user(name, password)
    print("got here")
    if request.method == "GET":

       
        print("I DEFINETLY GOT HERE!")
        return render_template("pops.html", user=name, pas=password)

       
    if request.method == "POST":
        uploaded_file = request.files['file']
 
        filename = secure_filename(uploaded_file.filename)
        
        file_name = str(uuid.uuid1()) + "_" + filename

        saver = request.files["file"]

        uploaded_file=file_name
        
        saver.save(os.path.join(app.config['UPLOAD_PAT'], filename))





        






        print (person.key())
        title = request.form.get("title") 
        title1 = request.form.get("title1")
        print(title)
        if title1 != title:
            return redirect("/login")
        if title1 == title:
            print("hej")
            music = {"title":title, "sound": "m", "file":filename}
            db.child("konto").child(person.key()).child("music").push(music)
            return render_template("pops.html", user=name, pas=password)

@app.route('/track', methods=['GET', 'POST'])
def track():
    name = request.cookies.get('username')
    password = request.cookies.get('password')
    person = user(name, password)
    file = person.val().get('file')
    musik = person.val().get("music")

    return render_template("track.html", user=name, pas=password, musik=musik, file= file)



if __name__=="__main__":
    app.run(debug=True)




