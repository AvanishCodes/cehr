from rest_framework import generics
from ..models import State
from ..serializers import StateSerializer


class StateCreateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateFilter(generics.ListAPIView):
    serializer_class = StateSerializer
    def get_queryset(self):

        country = self.kwargs['country']
        if country:
            return State.objects.filter(country=country)
        else:
            return State.objects.all()
    