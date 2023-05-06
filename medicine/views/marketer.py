# medicine/views/Marketer.py
from rest_framework import generics

# from django_filters import rest_framework as filters

from ..models import Marketer
from ..serializers import MarketerSerializer
# from ..filters import MarketerFilter
from ..pagination import DefaultPagination


class MarketerListCreate(generics.ListCreateAPIView):
    queryset = Marketer.objects.all()
    serializer_class = MarketerSerializer
    # filter_class = MarketerFilter
    pagination_class = DefaultPagination
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = MarketerFilter


class MarketerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marketer.objects.all()
    serializer_class = MarketerSerializer
    # filter_class = MarketerFilter


__all__ = (
    MarketerListCreate,
    MarketerDetail,
)