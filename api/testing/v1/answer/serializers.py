from rest_framework import serializers
from rest_framework_bulk import BulkListSerializer
from rest_framework_bulk.serializers import BulkSerializerMixin

from testing import models


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer


class AnswerBulkSerializer(AnswerSerializer, BulkSerializerMixin):
    class Meta(AnswerSerializer.Meta):
        list_serializer_class = BulkListSerializer
