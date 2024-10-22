# Description: This file contains the URL patterns for the house_management_api app.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/account/", include("account.urls")),

]
