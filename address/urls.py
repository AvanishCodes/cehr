# address/urls.py
from django.urls import path
from .views import (
    AddressCreateList,
    AddressRetrieveUpdateDestroy,
    CityCreateList,
    CityRetrieveUpdateDestroy,
    StateCreateList,
    StateRetrieveUpdateDestroy,
    CountryCreateList,
    CountryRetrieveUpdateDestroy,
)

urlpatterns = [
    # Address Model generics
    path('', AddressCreateList.as_view()),
    path('<int:pk>/', AddressRetrieveUpdateDestroy.as_view()),
]

# Export the urls
__all__ = [
    urlpatterns,
]
