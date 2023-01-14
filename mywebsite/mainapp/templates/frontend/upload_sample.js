function clicked(button) {
  var url = document.getElementsByClassName("url-button")[0];
  var file = document.getElementsByClassName("file-button")[0];

  if (url.style.background != "white" && button === "url-button") {
    url.style.background = "white";
    file.style.background = "#E5E8EB";
    document.getElementsByClassName("drag-box")[0].style.display = "none";
    document.getElementsByClassName("url-box")[0].style.display = "inline";
    url.style.cursor = "default";
    url.style.color = "black";
    file.style.cursor = "pointer";
  }

  if (file.style.background != "white" && button === "file-button") {
    file.style.background = "white";
    url.style.background = "#E5E8EB";
    document.getElementsByClassName("drag-box")[0].style.display = "flex";
    document.getElementsByClassName("url-box")[0].style.display = "none";
    file.style.cursor = "default";
    file.style.color = "black";
    url.style.cursor = "pointer";
  }
}
function purple(element) {
  button = document.getElementsByClassName(element)[0];
  console.log(button.style.background);
  if (button.style.background != "white") {
    button.style.color = "#712DC8";
  }
}
function black(element) {
  document.getElementsByClassName(element)[0].style.color = "black";
}

let circularProgress = document.querySelector(".circular-progress"),
progressValue = document.querySelector(".progress-value");

let progressStartValue = 0,    
progressEndValue = 90,    
speed = 30;

let progress = setInterval(() => {
progressStartValue++;

progressValue.textContent = `${progressStartValue}%`
circularProgress.style.background = `conic-gradient(#00843D ${progressStartValue * 3.6}deg, #ededed 0deg)`

if(progressStartValue == progressEndValue){
    clearInterval(progress);
}    
}, speed);