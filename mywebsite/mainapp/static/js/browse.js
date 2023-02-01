const box = document.getElementsByClassName("drag-box")[0];
const browse = document.getElementById("browse");

const uploadedFile = document.getElementById("uploaded-file");
const fileName = document.getElementById("file-name");
const fileSize = document.getElementById('file-size');
const closeFile = document.getElementById('close-file');

uploadedFile.style.display = 'none';

box.addEventListener("click", () => {
  if (browse.value == browse.defaultValue){
  browse.click();
  
}
});

browse.onchange = () => {
    const selectedFile = browse.files[0];
    fileName.innerHTML = selectedFile['name'];
    fileSize.innerText = getSize(selectedFile.size.toString());

    box.style.display = 'none';
    uploadedFile.style.display = "flex";

    console.log(selectedFile['name']);
    console.log(browse.files[0]);
  }

  closeFile.addEventListener("click", () => {
    if (browse.value != browse.defaultValue){
      browse.value = browse.defaultValue;
      box.style.display = 'flex';
      uploadedFile.style.display = 'none';
      dragText.innerText = "اسحب الملف هنا";
    dragText.style.color = "black";
    }
   
  });
  
  // fileName.innerHTML = "new.json";
  // fileSize.innerText = "552 MB";
  function getSize(fileSize){
    if(fileSize.length < 7) return `${Math.round(+fileSize/1024).toFixed(1)} KB`
    return `${(Math.round(+fileSize/1024)/1000).toFixed(1)} MB`
  }
