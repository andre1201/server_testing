import django_filters
from rest_framework import filters

from testing.models import Test


class TestFilter(filters.FilterSet):

    class Meta:
        model = Test
