from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model()
class TenantRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for tenant registration by a landlord.
    """

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
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

