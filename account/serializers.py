from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class TenantRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for tenant registration by a landlord.
    """

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "phone_number",
        ]

    def create(self, validated_data):
        """
        Create a tenant user with the validated data and default password.
        """
        # Default password for tenant users.
        default_password = "password123!"

        # create a tenant user with the validated data and role.
        user = User.objects.create_user(
            **validated_data,
            role = User.TENANT,
        )

        # Set the password for the tenant user and saves the user.
        user.set_password(default_password)
        user.save()
        
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user model.
    """

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "role",
        ]
        read_only_fields = ["role", "id"]


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for changing the password.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        """
        Validate the new password.
        """
        validate_password(value)
        return value