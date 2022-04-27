from hashlib import sha256
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from tasks.validations.validations import Validation
from tasks.models import User

def login(request: HttpRequest) -> HttpResponse:
    if(request.session.has_key('user')):
        return redirect('/')
    elif(request.method == "POST"):
        return submitLogin(request)
    return render(request, 'auth/login.html', {'title': 'register', 'emailValidationMessage': ' ', 'passwordValidationMessage': ' '})


def submitLogin(request: HttpRequest) -> HttpResponse:
    email = request.POST['email'].strip()
    password = request.POST['password'].strip()
    hashedPassword = sha256(password.encode()).hexdigest()
    emailValidationMessage = Validation(email).validateEmail().message.strip()
    passwordValidationMessage = Validation(password).validatePassword(6, 15).message.strip()
    try:
        if(emailValidationMessage != "" or passwordValidationMessage != ""):
           raise Exception("Validation Errors")
        existUser = User.objects.filter(email = email).values().first()
        if(not existUser):
            raise Exception("User is not found")
        elif(hashedPassword != existUser['password']):
            raise Exception("Password or Email is not correct")
        request.session["user"] = {
            'id': existUser['id'],
            'email': existUser['email'],
            'name': existUser['name']
        }
        return redirect("index")
    except Exception as err:
        return render(request, 'auth/login.html', {'title': 'register', 'emailValidationMessage': emailValidationMessage, 'passwordValidationMessage': passwordValidationMessage, 'error': err.args[0]})

def logout(request: HttpRequest) -> HttpResponse:
    del request.session['user']
    return redirect('/')