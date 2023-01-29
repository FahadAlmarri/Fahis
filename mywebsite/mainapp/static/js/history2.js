const login = document.getElementsByClassName('history')[0];
login.style.borderBottom='2px solid #712dc8';
var leftButton = document.getElementById("left");
var rightButton = document.getElementById("right");
console.log(1)
leftButton.addEventListener('click', ()=> {
    var pageNumber = document.getElementById('page_number');
    if(pageNumber.textContent>0){
    pageNumber.textContent--
    }
    console.log(pageNumber.textContent)
 });
 rightButton.addEventListener('click', ()=> {
    var pageNumber = document.getElementById('page_number');
    pageNumber.textContent++
    console.log(pageNumber.textContent)
 });