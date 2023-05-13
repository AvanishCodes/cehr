from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from django_filters import rest_framework as filters

from centralised_services.services import BaseManageView
from ..models import State
from ..serializers import StateSerializer
from ..filters import StateFilter


class StateCreate(generics.CreateAPIView):
    queryset = State.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = StateSerializer


class StateList(generics.ListAPIView):
    queryset = State.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = StateSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = StateFilter


class StateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


# class StateFilter(generics.ListAPIView):
#     serializer_class = StateSerializer
#
#     def get_queryset(self):
#
#         country = self.kwargs['country']
#         if country:
#             return State.objects.filter(country=country)
#         else:
#             return State.objects.all()


class StateManageView(BaseManageView):
    VIEWS_BY_METHOD = {
        'GET': StateList.as_view,
        'POST': StateCreate.as_view,
    }
