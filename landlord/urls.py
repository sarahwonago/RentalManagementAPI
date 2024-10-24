from django.urls import path
from rest_framework import routers

from .views import TenantViewSet

router = routers.DefaultRouter()
router.register(r'tenant', TenantViewSet, basename='tenant')

urlpatterns = router.urls