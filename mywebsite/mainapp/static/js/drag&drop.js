const dragBox = document.querySelector('.drag-box');
const input = document.getElementById("browse");
const dragText = document.getElementById("drag-text");


dragBox.addEventListener('dragover', (event)=>{
    event.preventDefault();
    console.log("dragover");
    
    dragText.innerText = "افلت الملف للرفع";
    dragText.style.color = "#712dc8";

})

dragBox.addEventListener('dragleave', ()=>{
    console.log("left");
    dragText.innerText = "اسحب الملف هنا";
    dragText.style.color = "black";
})

dragBox.addEventListener('drop', (event)=>{
    event.preventDefault();
    console.log("dropped");
    
    input.files = event.dataTransfer.files;
    input.onchange()
    console.log(input.files[0]);
})