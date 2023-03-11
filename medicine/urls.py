# medicine/urls.py

from django.urls import path

from .views import (
    MoleculeListCreate,
    MolecularDetail,
)

urlpatterns = [
    path('molecules/', MoleculeListCreate.as_view(), name='molecule-list'),
    path('molecules/<int:pk>/', MolecularDetail.as_view(), name='molecule-detail'),
]