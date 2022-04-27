const addAnswersFieldsInput = document.querySelector('.add_answers_fields')
const confirmAnswersFieldsBtn = document.querySelector('.confirm_answers_fields')
//------
const questionInput = document.querySelector('.question')
const correctAnswerInput = document.querySelector('.correctAnswer')
//------
const wrongAnswersFields = []
const questionErrorMessage = document.querySelector('.questionErrorMessage')
const correctErrorMessage = document.querySelector('.correctErrorMessage')
const errorMessage = document.querySelector('.errorMessage')
//------
const answersFieldsContainer = document.getElementById('answers_fields')
//------
const addBtn = document.querySelector('.addQuestion')

questionErrorMessage.innerHTML = " "
correctErrorMessage.innerHTML = " "
errorMessage.innerHTML = " "


const disableBtn = () => {
    if(questionErrorMessage.innerHTML != "" || correctErrorMessage.innerHTML != "" || errorMessage.innerHTML != "") {
        addBtn.setAttribute("disabled", true)
    }else {
        addBtn.removeAttribute("disabled")
    }
}

disableBtn()

questionInput.addEventListener('keyup', (e)=>{
    validateStringOnChange(e.target.value, "Question", questionErrorMessage, true, 3, 100, true, true, false)
    disableBtn()
})

correctAnswerInput.addEventListener('keyup', (e)=> {
    validateStringOnChange(e.target.value, "Corect answer", correctErrorMessage, true, 3, 100, true, true, false)
    disableBtn()
})



confirmAnswersFieldsBtn.addEventListener('click', ()=> {
    for(let i=1; i <= addAnswersFieldsInput.value; i++) {
        let answerField = document.createElement('input')
        answersFieldsContainer.insertBefore(answerField, addBtn)
        answerField.classList.add('form-control', 'wrong_answers_fields', 'mt-2')
        answerField.setAttribute('type', 'text')
        answerField.setAttribute('name', `answer${i}`)
        answerField.setAttribute('placeholder', `Wrong answer ${i}`)
        wrongAnswersFields.push(answerField)
    }

    for(let i= 0; i< wrongAnswersFields.length; i++){
        wrongAnswersFields[i].addEventListener('keyup', (e) => {
            validateStringOnChange(e.target.value, `Answer ${wrongAnswersFields[i].name}`, errorMessage, true, 3, 100, true, true, false)
            disableBtn()
        })
    }
})






