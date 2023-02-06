const emailError = document.querySelector(".email-error");
const emailInput = document.getElementsByClassName("text-field")[3];

const passField = document.querySelector(".password-error");
const passInput = document.getElementsByClassName("text-field")[4];
(cPassField = document.querySelector(".confirm-error")),
  (cPassInput = document.getElementsByClassName("text-field")[5]);
const form = document.querySelector("form");

// Email Validtion
function checkEmail() {
  const emaiPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  if (!emailInput.value.match(emaiPattern)) {
    return emailError.classList.add("invalid"); //adding invalid class if email value do not mathced with email pattern
  }
  emailError.classList.remove("invalid"); //removing invalid class if email value matched with emaiPattern
  console.log("correct");
}
// Password Validation
function createPass() {
  const passPattern =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&:.^;:',-_])[A-Za-z\d@$!%*?&:.^;:',-_]{8,}$/;

  if (!passInput.value.match(passPattern)) {
    return passField.classList.add("invalid"); //adding invalid class if password input value do not match with passPattern
  }
  passField.classList.remove("invalid"); //removing invalid class if password input value matched with passPattern
}

// Confirm Password Validtion
function confirmPass() {
  if (passInput.value !== cPassInput.value || cPassInput.value === "") {
    return cPassField.classList.add("invalid");
  }
  cPassField.classList.remove("invalid");
}
// Calling Funtion on Form Sumbit
form.addEventListener("submit", (e) => {
   //preventing form submitting
  checkEmail();
  createPass();
  confirmPass();

  //calling function on key up
  emailInput.addEventListener("keyup", checkEmail);
  passInput.addEventListener("keyup", createPass);
  cPassInput.addEventListener("keyup", confirmPass);

  if (
    emailError.classList.contains("invalid") ||
    passField.classList.contains("invalid") ||
    cPassField.classList.contains("invalid")
  ) {
    e.preventDefault();
  }
});