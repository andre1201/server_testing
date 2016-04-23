from rest_framework import serializers
from rest_framework_bulk import BulkListSerializer
from rest_framework_bulk.serializers import BulkSerializerMixin

from testing import models


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question


class QuestionBulkSerializer(QuestionSerializer, BulkSerializerMixin):
    class Meta(QuestionSerializer.Meta):
        list_serializer_class = BulkListSerializer
