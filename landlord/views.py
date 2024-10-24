from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from account.permissions import IsLandLord
from account.serializers import UserSerializer

from tenant.serializers import TenantRegistrationSerializer
from tenant.models import Tenant

from django.contrib.auth import get_user_model

User = get_user_model()

class TenantViewSet(viewsets.ModelViewSet):
    """
    Viewset for landlords to manage tenants they have registered.
    Only landlords can register new tenants and manage tenants linked to them.
    """
    serializer_class = TenantRegistrationSerializer
    permission_classes = [IsAuthenticated, IsLandLord]
    queryset = Tenant.objects.all()

    def get_queryset(self):
        # Fetch tenants linked to the current landlord
        return Tenant.objects.filter(landlord=self.request.user)

    def perform_create(self, serializer):
        # Create a tenant and link them to the landlord
        serializer.save(landlord=self.request.user)
