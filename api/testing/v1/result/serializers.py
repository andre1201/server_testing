from rest_framework_bulk import BulkListSerializer
from rest_framework_bulk.serializers import BulkSerializerMixin

from python_commons.commons.rest.serializers import OwnerSerializer
from testing import models


class ResultSerializer(OwnerSerializer):
    class Meta:
        model = models.Result


class ResultBulkSerializer(ResultSerializer, BulkSerializerMixin):
    class Meta(ResultSerializer.Meta):
        list_serializer_class = BulkListSerializer
