# coding=utf-8
from __future__ import unicode_literals

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView

from python_commons.commons.rest.mixins import FilterMixin, LoggerMixinView
from testing import models
from . import serializers


class ListView(LoggerMixinView, FilterMixin, ListBulkCreateUpdateDestroyAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionBulkSerializer


class SingleView(LoggerMixinView, RetrieveUpdateDestroyAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
