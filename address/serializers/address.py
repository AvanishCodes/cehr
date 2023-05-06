from rest_framework import serializers
from ..models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'al1', 'al2', 'city', 'state', 'pincode')
        read_only_fields = ('id',)
