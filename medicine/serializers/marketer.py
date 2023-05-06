# medicine/serializers/marketer.py

from rest_framework import serializers
from ..models import Marketer


class MarketerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketer
        fields = ('id', 'shorthand', 'name', 'address',)
        read_only_fields = ('id',)


__all__ = (
    MarketerSerializer,
)
