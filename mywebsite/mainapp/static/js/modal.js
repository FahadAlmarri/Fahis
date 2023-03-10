const openModalButton = document.getElementById("next-button");
 const closeModalButton = document.getElementById('close');
 const overlay = document.getElementById("overlay");

 openModalButton.addEventListener('click', ()=> {
    const modal = document.getElementById('modal');
    openModal(modal);
 });

 
closeModalButton.addEventListener('click', ()=> {
    const modal = document.getElementById('modal');
    closeModal(modal);
 });

 

overlay.addEventListener('click', ()=>{
    const modal = document.getElementById('modal');
    closeModal(modal);
})

function openModal(modal){
    if(modal == null) return
    modal.classList.add('active');
    overlay.classList.add('active');
    console.log('open')
    const url = document.getElementById("url")
    const textField = document.querySelector(".text-field");
    url.value = textField.value;
    console.log(url.value)
  }
  function closeModal(modal){
    if(modal == null) return
    modal.classList.remove('active');
    overlay.classList.remove('active');
  }