# This file contains the URL patterns for the house_management_api app.

from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView, 
    SpectacularSwaggerView
)


urlpatterns = [
    # admin panel
    path("admin/", admin.site.urls),

    # api documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # user management
    path("api/account/", include("account.urls")),

    # landlord-tenant management
    #path("api/landlord/", include("landlord.urls")),

]
