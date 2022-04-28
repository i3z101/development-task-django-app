const answerRadioInputs = document.querySelectorAll('.answer')
const submitAnswerBtn = document.querySelector('.submit_answer')


for(let i= 0; i < answerRadioInputs.length; i++) {
    answerRadioInputs[i].addEventListener('change', (e) => {
        if(e.target.checked) {
            submitAnswerBtn.removeAttribute('disabled')
        }
    })
}
