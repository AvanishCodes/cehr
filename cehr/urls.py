"""cehr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as gsv
from drf_yasg import openapi

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

schema_view = gsv(
    openapi.Info(
        title="Community EHR Solutions",
        default_version='v0.1',
        description="EHR Service API Documentation",
        terms_of_service="https://github.com/AvanishCodes/cehr/blob/main/LICENSE.md",
        contact=openapi.Contact(email="avanishcodes@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),
    # API Documentation
    path(
        '',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui(
            'redoc',
            cache_timeout=0
        ),
        name='schema-redoc'
    ),
    # Monitoring
    path('', include('django_prometheus.urls')),

    # Django Application Modules
    path('address/', include('address.urls')),
    path('auth/', include('authentication.urls')),
    path('doctor/', include('doctor.urls')),
    path('medicine/', include('medicine.urls')),

]


urlpatterns += staticfiles_urlpatterns()