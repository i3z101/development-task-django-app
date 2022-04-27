"""djangoTasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from tasks.controllers import indexController,registerController, loginController, questionsController
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', indexController.home, name='index'),
    path('register', registerController.register, name='register'),
    path('login', loginController.login, name='login'),
    path('add-question', questionsController.addQuestion, name='add-question'),
    path('questions/<question_id>', questionsController.questionDetails, name='question-details'),
    path('logout', loginController.logout, name='logout'),
]
