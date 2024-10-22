from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TenantViewSet

router = DefaultRouter()
router.register(r"tenants", TenantViewSet, basename="tenant")

urlpatterns = router.urls