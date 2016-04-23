# coding=utf-8
from __future__ import unicode_literals

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView

from commons.mixins import FilterMixin
from testing import models
from . import serializers


class ListView(FilterMixin, ListBulkCreateUpdateDestroyAPIView):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultBulkSerializer


class SingleView(RetrieveUpdateDestroyAPIView):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
