
let circularProgress = document.querySelector(".circular-progress"),
progressValue = document.querySelector(".progress-value");

let progressStartValue = 0,    
progressEndValue = document.querySelector(".progress-end").textContent,    
speed = 30;

let progress = setInterval(() => {


console.log(document.querySelector(".progress-end").textContent)
progressValue.textContent = `${progressStartValue}%`
circularProgress.style.background = `conic-gradient(var(--result-color) ${progressStartValue * 3.6}deg, #ededed 0deg)`

if(progressStartValue == progressEndValue){
    clearInterval(progress);
}    
progressStartValue++;
}, speed);


let root = document.documentElement;
const decision = document.querySelector(".result-decision");

console.log(progressEndValue);


progressEndValue = 40;
result_ranges(50, 80);


function result_ranges(red, green){
    if (progressEndValue > green){ //green

    }else if(progressEndValue > red){ //yellow
        root.style.setProperty('--result-color', "rgb(173, 100, 5)");
        decision.innerHTML = "مشتبه به";
    }else{ // red
        root.style.setProperty('--result-color', "red");
        decision.innerHTML = "خطر";

    }

}


/*----- details navbar */
const processesButton = document.getElementsByClassName('processes-button')[0];
const networkButton = document.getElementsByClassName('network-button')[0];
const processesTable = document.getElementsByClassName('processes-table')[0];
const networkTable = document.getElementsByClassName('network-table')[0];


networkTable.style.display = "none"

processesButton.addEventListener('click',()=>{
    if (networkButton.style.color != "black"){

        processesTable.style.removeProperty( 'display' );
        networkTable.style.display = "none";

        processesButton.style.borderBottom = "2px solid #712dc8";
        processesButton.style.color = "#712dc8";

        networkButton.style.border = "none";
        networkButton.style.color = "black";
        
    }
});

networkButton.addEventListener('click',()=>{
    if (processesButton.style.color != "black"){

        networkTable.style.removeProperty( 'display' );
        processesTable.style.display = "none";

        networkButton.style.borderBottom = "2px solid #712dc8";
        networkButton.style.color = "#712dc8";

        processesButton.style.border = "none";
        processesButton.style.color = "black";
        
    }
});

