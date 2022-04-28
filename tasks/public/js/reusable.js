const redirect = document.getElementById('redirect');
const modalContainer = document.getElementById('register-modal')
const modalOverlay = document.getElementById('modal-overlay')

if(modalContainer != null) {
    modalContainer.classList.add('fade', 'show')
    modalContainer.setAttribute('role', 'dialog')
    modalContainer.setAttribute('aria-modal', true)
    modalContainer.removeAttribute('aria-hidden')
    modalContainer.style.display = 'block'
    modalOverlay.classList.add('show')
    setTimeout(()=> {
        window.location.href = `${redirect.value}`
    }, 2000)
}