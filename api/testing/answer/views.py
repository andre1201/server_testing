from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView

from commons.mixins import FilterMixin
from testing import models
from . import serializers


class ListView(FilterMixin, ListBulkCreateUpdateDestroyAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerBulkSerializer


class SingleView(RetrieveUpdateDestroyAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
