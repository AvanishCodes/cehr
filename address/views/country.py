from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from centralised_services.services import BaseManageView
from ..models import Country
from ..serializers import CountrySerializer


class CountryCreate(generics.CreateAPIView):
    queryset = Country.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = CountrySerializer


class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CountrySerializer


class CountryRetrieve(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CountrySerializer


class CountryManageView(BaseManageView):
    VIEWS_BY_METHOD = {
        'GET': CountryList.as_view,
        'POST': CountryCreate.as_view,
    }
