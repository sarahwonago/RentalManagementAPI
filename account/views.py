
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from drf_spectacular.utils import extend_schema, extend_schema_view

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (
    ChangePasswordSerializer, 
    LandlordRegistrationSerializer
    )
from .permissions import IsSuperAdmin


User = get_user_model()


@extend_schema_view(
    create=extend_schema(
        summary="Register a new landlord",
        description="Create a new user with the 'landlord' role.",
        responses={201: LandlordRegistrationSerializer},
        request=LandlordRegistrationSerializer,
    ),
    list=extend_schema(
        summary="List all landlords",
        description="Retrieve a list of all registered landlords.",
        responses={200: LandlordRegistrationSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Retrieve a landlord",
        description="Retrieve details of a specific landlord by UUID.",
        responses={200: LandlordRegistrationSerializer},
    ),
    update=extend_schema(
        summary="Update a landlord",
        description="Update details of a specific landlord.",
        responses={200: LandlordRegistrationSerializer},
    ),
    destroy=extend_schema(
        summary="Delete a landlord",
        description="Delete a specific landlord.",
        responses={204: None},
    ),
)
class LandlordViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing landlords.
    
    All users registered via this endpoint will have the 'landlord' role.
    """

    queryset = User.objects.filter(role=User.LANDLORD)
    serializer_class = LandlordRegistrationSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    # filtering, searching and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter

    ]
    filterset_fields = ['email', 'first_name', 'last_name']
    search_fields = ['email', 'first_name', 'last_name', 'username']
    ordering_fields = ['date_joined', 'first_name']
    ordering = ['date_joined']

    def create(self, request, *args, **kwargs):
        """
        Register a landlord by creating a new user with 'landlord' role.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED
            )
    
    

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

        return Response(
            {"message":"Password changed successfully."}, 
            status=status.HTTP_200_OK
            )