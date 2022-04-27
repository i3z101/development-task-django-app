from asyncio.windows_events import NULL
import json
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from tasks.models import Question, User
from tasks.validations.validations import Validation
from django.contrib import messages

def addQuestion(request: HttpRequest) -> HttpResponse:
    if(request.method == "POST"):
        return submitQuestion(request)
    return render(request, 'add-question.html', {'title': 'Add Question'})

def submitQuestion(request: HttpRequest) -> HttpResponse:
    userSession = request.session.get("user")
    answers: list = []
    numQuestions: str = request.POST['numQuestions']
    numQuestionsValidationMessage = Validation(numQuestions).validateNumeric("Number of wrong answers", True).message.strip()
    question: str = request.POST['question']
    questionValidationMessage: str = Validation(question).validateString("Question", True, 3, 100, True, True).message.strip()
    correctAnswer: str = request.POST['correctAnswer']
    correctAnswerValidationMessage: str = Validation(correctAnswer).validateString("Correct Answer", True, 3, 100, True, True).message.strip()
    if(numQuestionsValidationMessage != "" or questionValidationMessage != "" or correctAnswerValidationMessage != ""):
        messages.info(request, numQuestionsValidationMessage)
        messages.info(request, questionValidationMessage)
        messages.info(request, correctAnswerValidationMessage)
        return redirect('/add-question')
    answers.append(correctAnswer)
    for i in range(int(numQuestions)):
        wrongAnswer = request.POST['answer' + str(i+1)]
        wrongAnswersValidations = Validation(wrongAnswer).validateString("Wrong answer " + str(i+1), True, 3, 100, True, True).message.strip()
        if(wrongAnswersValidations != ""):
            messages.info(request, wrongAnswersValidations)
            return redirect('/add-question')
        answers.append(wrongAnswer)
    encodedAnswers = json.dumps(answers)
    newQuestion = Question(question= question, correctAnswer = correctAnswer, answers = encodedAnswers, user = User(id = userSession['id']))
    newQuestion.save()
    return redirect('/')

def questionDetails(request: HttpRequest, question_id: int) -> HttpResponse:
    if(request.method == 'POST'):
        return submitAnswer(request, question_id)
    question = Question.objects.filter(id = question_id).select_related('user').all().first()
    decodedAnswers = json.loads(question.answers)
    return render(request, 'question.html', {
        'title': 'Answer',
        'question': question,
        'answers': decodedAnswers
    })

def submitAnswer(request: HttpRequest, question_id: int) -> HttpResponse:
    question = Question.objects.filter(id = question_id).all().first()
    submittedAnswer = request.POST['answer']
    decodedAnswers = json.loads(question.answers)
    if(question.correctAnswer == submittedAnswer):
        return render(request, 'question.html', {
            'title': 'Answer',
            'question': question,
            'answers': decodedAnswers,
            'succeed': True 
            })
    return render(request, 'question.html', {
            'title': 'Answer',
            'question': question,
            'answers': decodedAnswers,
            'failed': True 
        })
    