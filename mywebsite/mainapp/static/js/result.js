let circularProgress = document.querySelector(".circular-progress"),
  progressValue = document.querySelector(".progress-value");

let progressStartValue = 0,
  progressEndValue = document.querySelector(".progress-end").textContent,
  speed = 30;
if (progressEndValue === "None") {
  progressValue.innerHTML = "-";
} else {
  let progress = setInterval(() => {
    console.log(document.querySelector(".progress-end").textContent);
    progressValue.textContent = `${progressStartValue}%`;
    circularProgress.style.background = `conic-gradient(var(--result-color) ${
      progressStartValue * 3.6
    }deg, #ededed 0deg)`;

    if (progressStartValue == progressEndValue) {
      clearInterval(progress);
    }
    progressStartValue++;
  }, speed);
}

let root = document.documentElement;
const decision = document.querySelector(".result-decision");

console.log(progressEndValue);

// progressEndValue = 70;
result_ranges(39, 69);

function result_ranges(green, red) {
  if (progressEndValue === "None") {
    root.style.setProperty("--result-color", "grey");
    decision.innerHTML = ".." + "قيد الفحص";
    $('#duration').text('-');
    return;
  }
  if (progressEndValue > red) {
    //red
    root.style.setProperty("--result-color", "red");
    decision.innerHTML = "خطر";
  } else if (progressEndValue > green) {
    //yellow
    root.style.setProperty("--result-color", "rgb(173, 100, 5)");
    decision.innerHTML = "مشتبه به";
  } else {
    // green
  }
}

/*----- details navbar */
const processesButton = document.getElementsByClassName("processes-button")[0];
const networkButton = document.getElementsByClassName("network-button")[0];
const screenshotsButton = document.getElementsByClassName("screenshots-button")[0];

const processesTable = document.getElementsByClassName("processes-table")[0];
const networkTable = document.getElementsByClassName("network-table")[0];
const screenshotsTable = document.getElementsByClassName("screenshots-table")[0];


networkTable.style.display = "none";
screenshotsTable.style.display = "none";

networkButton.style.color = "black";
screenshotsButton.style.color = "black";

processesButton.addEventListener("click", () => {
  if (processesButton.style.color == "black") {
    processesTable.style.removeProperty("display");
    networkTable.style.display = "none";
    screenshotsTable.style.display = "none";

    processesButton.style.borderBottom = "2px solid #712dc8";
    processesButton.style.color = "#712dc8";

    networkButton.style.border = "none";
    networkButton.style.color = "black";
    screenshotsButton.style.border = "none";
    screenshotsButton.style.color = "black";
  }
});

screenshotsButton.addEventListener("click", () => {
  if (screenshotsButton.style.color == "black") {
    screenshotsTable.style.removeProperty("display");
    processesTable.style.display = "none";
    networkTable.style.display = "none";

    screenshotsButton.style.borderBottom = "2px solid #712dc8";
    screenshotsButton.style.color = "#712dc8";

    processesButton.style.border = "none";
    processesButton.style.color = "black";
    networkButton.style.border = "none";
    networkButton.style.color = "black";
  }
});

networkButton.addEventListener("click", () => {
  if (networkButton.style.color == "black") {
    networkTable.style.removeProperty("display");
    processesTable.style.display = "none";
    screenshotsTable.style.display = "none";

    networkButton.style.borderBottom = "2px solid #712dc8";
    networkButton.style.color = "#712dc8";

    processesButton.style.border = "none";
    processesButton.style.color = "black";
    screenshotsButton.style.border = "none";
    screenshotsButton.style.color = "black";
  }
});
/*------- details content-------------*/

const ip = document.querySelectorAll(".ip").forEach(function (element) {
  if (element.innerText == "") element.innerText = "-";
});

/***counter */

numbering()
function numbering() {
  count = 1;
  const rows = document
    .querySelectorAll(".counter")
    .forEach(function (element) {
      element.innerText = count;
      count++;
    });
}
