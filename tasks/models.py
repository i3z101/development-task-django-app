from dataclasses import field
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)


class Question(models.Model):
    question = models.CharField(max_length=255)
    answers = models.TextField()
    correctAnswer = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    