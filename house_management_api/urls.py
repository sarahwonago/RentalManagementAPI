# Description: This file contains the URL patterns for the house_management_api app.
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)



urlpatterns = [
    path("admin/", admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path("api/account/", include("account.urls")),

]
