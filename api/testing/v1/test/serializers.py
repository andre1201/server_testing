from rest_framework import serializers
from rest_framework_bulk import BulkListSerializer
from rest_framework_bulk.serializers import BulkSerializerMixin

from testing import models


class TestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = models.Test


class TestBulkSerializer(TestSerializer, BulkSerializerMixin):
    class Meta(TestSerializer.Meta):
        list_serializer_class = BulkListSerializer
