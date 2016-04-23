from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView

from commons.mixins import FilterMixin, LoggerMixinView
from testing import models
from . import serializers


class ListView(LoggerMixinView, FilterMixin, ListBulkCreateUpdateDestroyAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerBulkSerializer


class SingleView(LoggerMixinView, RetrieveUpdateDestroyAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
