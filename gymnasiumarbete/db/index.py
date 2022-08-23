from dotenv import load_dotenv
import os
import pyrebase

load_dotenv()

config ={
 "apiKey": "AIzaSyCd0d3eR4E39e8HN3QnK55X0E_fdZptBEA",
  "authDomain": "test-34557.firebaseapp.com",
  "projectId": "test-34557",
  "storageBucket": "test-34557.appspot.com",
  "messagingSenderId": "199653041793",
  "appId": "1:199653041793:web:c4ecbd506e688da3540f80",
  "measurementId": "G-R3MC55QS4E",
  "databaseURL": "https://test-34557-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
