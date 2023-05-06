from rest_framework import serializers
from ..models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'state', 'country')
        read_only_fields = ('id',)
