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
    
    path('country/', CountryCreateList.as_view()),
    path('country/<int:pk>/', CountryRetrieveUpdateDestroy.as_view()),

    path('state/', StateCreateList.as_view()),
    path('state/<int:pk>/', StateRetrieveUpdateDestroy.as_view()),

    path('city/', CityCreateList.as_view()),
    path('city/<int:pk>/', CityRetrieveUpdateDestroy.as_view()),
]

# Export the urls
__all__ = [
    urlpatterns,
]
