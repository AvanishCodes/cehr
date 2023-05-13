from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django_filters import rest_framework as filters

from centralised_services.services import BaseManageView
from ..models import City
from ..serializers import CitySerializer
from ..filters import CityFilter


class CityCreate(generics.CreateAPIView):
    queryset = City.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CitySerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CityFilter


class CityRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


# add  a GET api for filtering cities by state/country


# class CityFilter(generics.ListAPIView):
#     serializer_class = CitySerializer
#
#     def get_queryset(self):
#
#         state = self.kwargs['state']
#         if state:
#             return City.objects.filter(state=state)
#         else:
#             return City.objects.all()


class CityManageView(BaseManageView):
    VIEWS_BY_METHOD = {
        'GET': CityList.as_view,
        'POST': CityCreate.as_view,
    }
