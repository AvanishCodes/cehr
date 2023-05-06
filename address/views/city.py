from rest_framework import generics
from ..models import City
from ..serializers import CitySerializer


class CityCreateList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# add  a GET api for filtering cities by state/country

class CityFilter(generics.ListAPIView):
    serializer_class = CitySerializer
    def get_queryset(self):

        state = self.kwargs['state']
        if state:
            return City.objects.filter(state=state)
        else:
            return City.objects.all()
