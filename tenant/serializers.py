from rest_framework import serializers

from django.contrib.auth import get_user_model

from account.serializers import UserSerializer

from tenant.models import Tenant


User = get_user_model()
class TenantRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for tenant registration by a landlord.
    """

    tenant = UserSerializer()
    landlord = serializers.StringRelatedField(required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "tenant",
            "landlord"
        ]

    def create(self, validated_data):
        """
        Create a tenant user with the validated data and default password.
        """
        # Default password for tenant users.
        default_password = "password123!"

        # Extract the tenant data from the validated data.
        user_data = validated_data.pop("tenant")
        # create a tenant user with the validated data and role.
        user = User.objects.create_user(
            **user_data,
            role = User.TENANT,
        )

        # Set the password for the tenant user and saves the user.
        user.set_password(default_password)
        user.save()

        # create the tenant object and link it with the user.
        tenant = Tenant.objects.create(
            tenant=user,
            **validated_data
        )
        
        return tenant

