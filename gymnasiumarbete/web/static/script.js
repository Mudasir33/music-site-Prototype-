




function get_full_Width (div){
    var style = getComputedStyle(div);
    var marginLeft = parseInt(style.marginLeft)
    var marginRight = parseInt(style.marginRight)
    
    return div.offsetWidth + marginRight + marginLeft


    

}



var carousels = document.getElementsByClassName("carousel")


for(var carousel of carousels) {
    
    carousel.setAttribute("length", 0)
    
    
    var span = carousel.getElementsByTagName("span")
 
    if (span.length<2) {
        console.log("skipar gallery")
        console.log(carousel)
        continue

        
        
    }
  
    span[1].onclick = (event)=>{
        var carousel = event.target.parentElement
        console.log(carousel)
        var l = carousel.getAttribute("length")
        var div = carousel.getElementsByTagName("div")
        l++;
        for (var boxen of div)
        {
            
            
            boxen.style.left = -get_full_Width(boxen)*l+"px"
            
            if (l>countSiblings(boxen)) {l=countSiblings(boxen);}
            
           
    
        }
        carousel.setAttribute("length",l)

    }
    
    span[0].onclick = ()=>{
        
        var carousel = event.target.parentElement
       
        var l = carousel.getAttribute("length")
        var div = carousel.getElementsByTagName("div")
        l--;
        for (var boxen of div)
        {
            boxen.style.left = -get_full_Width(boxen)*l+"px"
            
            
            if (l<0) {l=0;}
    
        }
        carousel.setAttribute("length",l)
    }
    
    
}

function countSiblings(boxen){
 
    return boxen.parentElement.childElementCount-5
}


