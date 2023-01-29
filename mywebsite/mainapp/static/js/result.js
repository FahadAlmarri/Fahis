
let circularProgress = document.querySelector(".circular-progress"),
progressValue = document.querySelector(".progress-value");

let progressStartValue = 0,    
progressEndValue = document.querySelector(".progress-end").textContent,    
speed = 30;

let progress = setInterval(() => {


console.log(document.querySelector(".progress-end").textContent)
progressValue.textContent = `${progressStartValue}%`
circularProgress.style.background = `conic-gradient(#00843D ${progressStartValue * 3.6}deg, #ededed 0deg)`

if(progressStartValue == progressEndValue){
    clearInterval(progress);
}    
progressStartValue++;
}, speed);