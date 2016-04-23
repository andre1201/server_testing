# coding=utf-8
from __future__ import unicode_literals

from urllib import urlencode

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView

from api.testing.test.filters import TestFilter
from commons.mixins import FilterMixin
from testing import models
from . import serializers


class ListView(FilterMixin, ListBulkCreateUpdateDestroyAPIView):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestBulkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SingleView(RetrieveUpdateDestroyAPIView):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer
