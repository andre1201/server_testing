from rest_framework_bulk import BulkListSerializer
from rest_framework_bulk.serializers import BulkSerializerMixin

from python_commons.commons.rest.serializers import OwnerSerializer
from testing import models


class TestSerializer(OwnerSerializer):
    class Meta:
        model = models.Test


class TestBulkSerializer(TestSerializer, BulkSerializerMixin):
    class Meta(TestSerializer.Meta):
        list_serializer_class = BulkListSerializer
