# coding=utf-8
from __future__ import unicode_literals

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView

from commons.mixins import FilterMixin, LoggerMixinView
from testing import models
from . import serializers


class ListView(LoggerMixinView, FilterMixin, ListBulkCreateUpdateDestroyAPIView):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestBulkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SingleView(LoggerMixinView, RetrieveUpdateDestroyAPIView):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer
