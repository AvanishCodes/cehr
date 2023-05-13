from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Address
from ..serializers import AddressSerializer


class AddressCreateList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AddressSerializer


class AddressRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
