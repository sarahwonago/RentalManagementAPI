from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TenantViewSet, ChangePasswordViewset

router = DefaultRouter()
router.register(r"tenants", TenantViewSet, basename="tenant")
router.register(r"change-password", ChangePasswordViewset, basename="change-password")

urlpatterns = router.urls