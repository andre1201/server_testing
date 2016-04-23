# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=200, help_text='Название теста')
    created = models.DateTimeField(auto_now=True, help_text='Дата создания')
    owner = models.ForeignKey(User, related_name='tests')


class Question(models.Model):
    title = models.CharField(max_length=200, help_text='Заголовок')
    test = models.ForeignKey(Test, related_name='questions')


class Answer(models.Model):
    title = models.CharField(max_length=200, help_text='Заголовок')
    is_true = models.BooleanField(default=False, help_text='Верный ответ')
    question = models.ForeignKey(Question, related_name='answers')


class Result(models.Model):
    grade = models.IntegerField(help_text='Оценка')
    correct_count = models.IntegerField(help_text='Количество правильных ответов')
    incorrect_count = models.IntegerField(help_text='Количество не правильных ответов')
    created = models.DateTimeField(auto_now=True, help_text='Дата прохождения')
    test = models.ForeignKey(Test, related_name='results')
    owner = models.ForeignKey(User, related_name='results')
