from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from drf_spectacular.utils import extend_schema, extend_schema_view

from .serializers import (UserSerializer, ChangePasswordSerializer, TenantRegistrationSerializer, LandlordRegistrationSerializer)
from .permissions import IsLandLord, IsTenant, IsSuperAdmin

User = get_user_model()

class LandlordViewSet(viewsets.ModelViewSet):
    """
    ViewSet for registering1 landlords.
    
    All users registered via this endpoint will have the 'landlord' role.
    """
    queryset = User.objects.filter(role=User.LANDLORD)
    serializer_class = LandlordRegistrationSerializer
    #permission_classes = [IsAuthenticated, IsSuperAdmin]

    def create(self, request, *args, **kwargs):
        """
        Register a landlord by creating a new user with 'landlord' role.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class TenantViewSet(viewsets.ModelViewSet):
    """
    Viewset for landlord to manage tenants.

    Only users with the role of landlord can register new tenants.
    """

    queryset = User.objects.filter(role=User.TENANT)
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated, IsLandLord]

    def create(self, request, *args, **kwargs):
        """
        Creates a tenant user.
        """

        serializer = TenantRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@extend_schema_view(
    create=extend_schema(
        summary="Change Password",
        description="Allows authenticated users to change their password. The users must provide the old password and a new password.",
        request=ChangePasswordSerializer,
        responses={
            200: 'Password changed successfully.',
            400: 'Bad request. Old password is incorrect or new password fails validation.',
        },
        tags=['password management'],
    ),
)
class ChangePasswordViewset(viewsets.ViewSet):
    """
    Viewset for tenants or landlord to change their passwords.

    Only users who are authenticated can change their passwords.
    """

    permission_classes = [IsAuthenticated]

    @extend_schema(
        description="Change password for authenticated user.",
        responses={200: 'Password changed successfully.', 400: 'Invalid old password or new password not valid.'},
        tags=['Password Management']
    )
    def create(self, request, *args, **kwargs):
        """
        Change the password of the authenticated user.
        """
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # checks if the old password matches
        user = request.user
        if not check_password(serializer.validated_data.get("old_password"), user.password):
            return Response({"old_password":"Wrong password."}, status=status.HTTP_400_BAD_REQUEST)
        
        # set the new password and save the user.
        user.set_password(serializer.validated_data.get("new_password"))
        user.save()

        return Response({"message":"Password changed successfully."}, status=status.HTTP_200_OK)