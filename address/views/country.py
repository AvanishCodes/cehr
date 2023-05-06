from rest_framework import generics
from ..models import Country
from ..serializers import CountrySerializer


class CountryCreateList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



class CountryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
