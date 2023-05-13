# address/urls.py
from django.urls import path
from .views import (
    AddressCreateList,
    AddressRetrieveUpdateDestroy,
    CityManageView,
    CityRetrieveUpdateDestroy,
    StateManageView,
    StateRetrieveUpdateDestroy,
    CountryManageView,
    CountryRetrieve,
)

urlpatterns = [
    # Address Model generics
    path('', AddressCreateList.as_view()),
    path('<int:pk>/', AddressRetrieveUpdateDestroy.as_view()),

    path('country/', CountryManageView.as_view()),
    path('country/<int:pk>/', CountryRetrieve.as_view()),

    path('state/', StateManageView.as_view()),
    path('state/<int:pk>/', StateRetrieveUpdateDestroy.as_view()),

    path('city/', CityManageView.as_view()),
    path('city/<int:pk>/', CityRetrieveUpdateDestroy.as_view()),
]

# Export the urls
__all__ = [
    urlpatterns,
]
