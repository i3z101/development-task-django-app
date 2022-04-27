from asyncio.windows_events import NULL
from email import message
from hashlib import sha1, sha256
from xml.dom import ValidationErr
from django.forms import RegexField
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.core.validators import EmailValidator
from tasks.models import User
from tasks.validations.validations import Validation


def register(request: HttpRequest) -> HttpResponse:
    if(request.session.has_key('user')):
        return redirect('/')
    elif(request.method == "POST"):
        return submitRegistration(request)
    return render(request, 'auth/register.html', {'title': 'register', 'emailValidationMessage': ' ', 'passwordValidationMessage': ' '})

def submitRegistration(request: HttpRequest) -> HttpResponse:
    name = request.POST['name'].strip()
    email = request.POST['email'].strip()
    password = request.POST['password'].strip()
    nameValidationMessage = Validation(name).validateString("Name", True, 3, 100, True, False).message.strip()
    emailValidationMessage = Validation(email).validateEmail().message.strip()
    passwordValidationMessage = Validation(password).validatePassword(6, 15).message.strip()
    try:
        existUser = User.objects.filter(email = email).exists()
        if(existUser):
            raise Exception("User is already registered")
        elif(emailValidationMessage != "" or passwordValidationMessage != "" or nameValidationMessage != ""):
            raise Exception("Validation Errors")
        hashedPassword = sha256(password.encode()).hexdigest()
        newUser = User()
        newUser.name = name
        newUser.email = email
        newUser.password = hashedPassword
        newUser.save()
        return render(request, 'auth/register.html', {'title': 'register', 'emailValidationMessage': ' ', 'passwordValidationMessage': ' ', 'succeed': True})
    except Exception as err:
        return render(request, 'auth/register.html', {'title': 'register', 'nameValidationMessage': nameValidationMessage, 'emailValidationMessage': emailValidationMessage, 'passwordValidationMessage': passwordValidationMessage, 'error': err.args[0]})