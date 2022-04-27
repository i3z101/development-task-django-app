const nameInput = document.querySelector('.name');
const nameValidation = document.querySelector('.nameValidation')
//------
const emailInput = document.querySelector('.email');
const emailValidation = document.querySelector('.emailValidation');
//------
const passwordInput = document.querySelector('.password');
const passwordValidation = document.querySelector('.passwordValidation')
//------
const submitBtn = document.querySelector('.submit');
//------
const errorMessage = document.querySelector('.errorMessage')
//------
const modalContainer = document.getElementById('register-modal')
const modalOverlay = document.getElementById('modal-overlay')

const disableBtn = () => {
    if(emailValidation.innerHTML != "" || passwordValidation.innerHTML != "") {
        submitBtn.setAttribute("disabled", true)
    }else {
        submitBtn.removeAttribute("disabled")
    }
}

disableBtn()

if(nameInput != null) {
    nameInput.addEventListener('keyup', (e)=> {
        validateStringOnChange(e.target.value, "Name", nameValidation, true, 3, 100, true, false, false)
    })
}


emailInput.addEventListener('keyup', (e) => {
    validateEmailOnChange(e.target.value, emailValidation, true);
    disableBtn()
})

passwordInput.addEventListener('keyup', (e) => {
    validatePasswordOnChange(e.target.value, passwordValidation, 6, 15)
    disableBtn()
})

if(modalContainer != null) {
    modalContainer.classList.add('fade', 'show')
    modalContainer.setAttribute('role', 'dialog')
    modalContainer.setAttribute('aria-modal', true)
    modalContainer.removeAttribute('aria-hidden')
    modalContainer.style.display = 'block'
    modalOverlay.classList.add('show')
    setTimeout(()=> {
        window.location.href = "/login"
    }, 2000)
}