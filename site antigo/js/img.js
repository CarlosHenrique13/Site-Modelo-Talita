function Zom(id){
    var img = document.getElementById(id);
    if (img.style.width === "80%"){
        img.style.width = "20%"
    }else{
        img.style.width = "80%"
    }
}