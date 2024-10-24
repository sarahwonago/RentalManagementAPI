from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ChangePasswordViewset, LandlordViewSet

router = DefaultRouter()
router.register(r"change-password", ChangePasswordViewset, basename="change-password")
router.register(r"landlord", LandlordViewSet, basename="landlord")

urlpatterns = [
    path("log-in/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]


urlpatterns += router.urls