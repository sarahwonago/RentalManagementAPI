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
    Viewset for landlord to manage tenants they have registered.

    Only users with the role of landlord can register new tenants.
    """

    queryset = User.objects.filter(role=User.TENANT)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsLandLord]

    def create(self, request, *args, **kwargs):
        """
        Creates a tenant user.
        """

        serializer = TenantRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tenant = serializer.save()

        # link tenant to landlord after saving tenant
        Tenant.objects.create(
            tenant=tenant,
            landlord=request.user
        )
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED
            )

    def list(self, request, *args, **kwargs):
        # override the tenants to display only tenants for this landlord.
        # role=tenant, landlord=request.user
        # tenants = Tenant.objects.filter(landlord=request.user)
        return super().list(request, *args, **kwargs)

