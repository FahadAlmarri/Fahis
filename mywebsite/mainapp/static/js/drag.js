const box = document.getElementsByClassName("drag-box")[0];
const browse = document.getElementById("browse");
const dragContent = document.getElementById("drag-content");
const h1 = document.getElementById("file-name");
box.addEventListener("click", () => {
  browse.click();
});

browse.onchange = () => {
    const selectedFile = browse.files[0];
    dragContent.style.display = 'none';
    h1.innerHTML = selectedFile['name'];
    console.log(selectedFile['name']);
  }
