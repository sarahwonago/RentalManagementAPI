from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from .serializers import UserSerializer, ChangePasswordSerializer, TenantRegistrationSerializer
from .permissions import IsLandLord, IsTenant

User = get_user_model()


class TenantViewSet(viewsets.ModelViewSet):
    """
    Viewset for landlord to manage tenants.

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
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

