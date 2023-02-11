const dragBox = document.querySelector('.drag-box');
const input = document.getElementById("browse");
const dragText = document.getElementById("drag-text");


dragBox.addEventListener('dragover', (event)=>{
    event.preventDefault();
    
    dragText.innerText = "افلت الملف للرفع";
    dragText.style.color = "#712dc8";

})

dragBox.addEventListener('dragleave', ()=>{
    dragText.innerText = "اسحب الملف هنا";
    dragText.style.color = "black";
})

dragBox.addEventListener('drop', (event)=>{
    event.preventDefault();

    input.files = event.dataTransfer.files;
    input.onchange()
})