# medicine/urls.py

from django.urls import path

from .views import (
    MoleculeListCreate,
    MolecularDetail,
    MarketerListCreate,
    MarketerDetail,
)

urlpatterns = [
    path('molecules/', MoleculeListCreate.as_view(), name='molecule-list'),
    path('molecules/<int:pk>/', MolecularDetail.as_view(), name='molecule-detail'),

    path('marketers/', MarketerListCreate.as_view(), name='marketer-list'),
    path('marketers/<int:pk>/', MarketerDetail.as_view(), name='marketer-detail'),
]