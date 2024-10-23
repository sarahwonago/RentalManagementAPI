from django.contrib import admin
from .models import CustomUser, Tenant

admin.site.register(CustomUser)
admin.site.register(Tenant)
