const history = document.getElementsByClassName("history")[0];
history.style.borderBottom = "2px solid #712dc8";

/* ---  paging -----*/
var leftButton = document.getElementById("left");
var rightButton = document.getElementById("right");
console.log(1);
leftButton.addEventListener("click", () => {
  var pageNumber = document.getElementById("page_number");
  if (pageNumber.textContent > 0) {
    pageNumber.textContent--;
  }
  console.log(pageNumber.textContent);
});
rightButton.addEventListener("click", () => {
  var pageNumber = document.getElementById("page_number");
  pageNumber.textContent++;
  console.log(pageNumber.textContent);
});

/* ----- switching (public, private) -----*/
const generalButton = document.getElementsByClassName("general-history")[0];
const privateButton = document.getElementsByClassName("your-history")[0];
const publicHistory = document.getElementsByClassName("public-history")[0];
const privateHistory = document.getElementsByClassName("private-history")[0];
const login = document.getElementsByClassName("login")[0];

generalButton.style.background="white";
privateHistory.style.display = "none";

generalButton.addEventListener("click", () => {
  publicHistoryClicked();
});



privateButton.addEventListener("click", () => {
  if(login.innerHTML == "تسجيل الدخول"){
    document.getElementById('history-anchor').click();
  }else{
    privateHistoryClicked();
  }
  
  
});







function publicHistoryClicked() {
  if (generalButton.style.background != "white") {
    generalButton.style.background = "white";
    privateButton.style.background = "#E5E8EB";

    privateHistory.style.display = "none";
    publicHistory.style.removeProperty( 'display' );

    generalButton.style.cursor = "default";
    privateButton.style.cursor = "pointer";

    generalButton.style.color = "black";
  }
}

function privateHistoryClicked() {
  if (privateButton.style.background != "white") {
    generalButton.style.background = "#E5E8EB";
    privateButton.style.background = "white";

    publicHistory.style.display = "none";
    privateHistory.style.removeProperty( 'display' );

    generalButton.style.cursor = "pointer";
    privateButton.style.cursor = "default";

    privateButton.style.color = "black";
  }
}


generalButton.addEventListener('mouseover',()=>{
  const color = generalButton.style.background;
  if (color != "white"){
    generalButton.style.color="#712DC8";
  }
});

generalButton.addEventListener('mouseout',()=>{
  generalButton.style.color="black";
});

privateButton.addEventListener('mouseover',()=>{
  const color = privateButton.style.background;
  if (color != "white"){
    privateButton.style.color="#712DC8";
  }
});

privateButton.addEventListener('mouseout',()=>{
  privateButton.style.color="black";
});



