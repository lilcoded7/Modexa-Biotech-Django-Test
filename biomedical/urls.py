"""
URL configuration for biomedical project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


# documentation import 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Bio Medical Test",
        default_version="v1",
        description="API documentation for Bio Medical Test",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)



urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('restapi.urls')),
    path('api/accounts/', include('accounts.urls'))
]


if settings.DEBUG:
    urlpatterns_extra = [
        path(
            "doc",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
    ]
    urlpatterns += urlpatterns_extra