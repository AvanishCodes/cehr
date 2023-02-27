from rest_framework import serializers
from ..models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'isd_code')
        read_only_fields = ('id',)
