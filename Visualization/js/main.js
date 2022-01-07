var btns = document.querySelectorAll(".buttons button");
var cat = document.getElementsByClassName("cat")[0];

for (i=0; i<btns.length; i++){
    btns[i].addEventListener("click",manageCatClasses);
}

function manageCatClasses(){
    if (this.getAttribute("data-add")) {
        cat.classList.add(this.getAttribute("data-add"))
    
    }
    if (this.getAttribute("data-remove")){
        cat.classList.remove(this.getAttribute("data-remove"))
    };

}
