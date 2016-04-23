from rest_framework import serializers
from rest_framework_bulk import BulkListSerializer
from rest_framework_bulk.serializers import BulkSerializerMixin

from testing import models


class ResultSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = models.Result


class ResultBulkSerializer(ResultSerializer, BulkSerializerMixin):
    class Meta(ResultSerializer.Meta):
        list_serializer_class = BulkListSerializer
