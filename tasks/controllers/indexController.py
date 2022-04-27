from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from tasks.models import Question, User


def home(request: HttpRequest)->HttpResponse:
    questions = Question.objects.select_related('user').all()
    return render(request, 'index.html', {'title': 'Home', 'questions': questions})