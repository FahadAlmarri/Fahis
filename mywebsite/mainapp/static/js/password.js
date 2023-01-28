const eye = document.getElementById("togglePassword");
const field = document.getElementById("password-field");
eye.addEventListener("click", () => {
    toggle();
});



function toggle() {
    console.log('working')
  if (field.getAttribute("type") === "password") {
    field.setAttribute("type", "text");
    eye.classList.remove('bi-eye');
    eye.classList.add('bi-eye-slash');
  } else {
    field.setAttribute("type", "password");
    eye.classList.remove('bi-eye-slash');
    eye.classList.add('bi-eye');
  }
}