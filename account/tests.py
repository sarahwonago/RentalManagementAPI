from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import CustomUser
import uuid

class CustomUserModelTest(TestCase):

    def setUp(self):
        # Creating initial test data
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass123",
            role=CustomUser.LANDLORD,
            phone_number="1234567890"
        )
    
    def test_user_creation(self):
        """
        Test that a user can be created and its fields are stored correctly.
        """
        user = self.user
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("testpass123"))
        self.assertEqual(user.role, CustomUser.LANDLORD)
        self.assertEqual(user.phone_number, "1234567890")
        self.assertTrue(isinstance(user.id, uuid.UUID))  # Check if UUID is used

    def test_user_roles(self):
        """
        Test that the user role is one of the predefined choices.
        """
        user = self.user
        self.assertIn(user.role, [CustomUser.LANDLORD, CustomUser.TENANT, CustomUser.SUPERADMIN])

    # def test_phone_number_uniqueness(self):
    #     """
    #     Test that phone numbers are unique across users.
    #     """
    #     with self.assertRaises(ValidationError):
    #         # Attempting to create another user with the same phone number
    #         user2 = CustomUser.objects.create_user(
    #             username="testuser2",
    #             email="testuser2@example.com",
    #             password="testpass123",
    #             role=CustomUser.TENANT,
    #             phone_number="1234567890"  # Same phone number as self.user
    #         )
    #         user2.full_clean()  # This will raise a ValidationError due to unique constraint

    def test_empty_phone_number_allowed(self):
        """
        Test that phone number can be blank or null.
        """
        user_with_no_phone = CustomUser.objects.create_user(
            username="nopho_user",
            email="nopho@example.com",
            password="testpass123",
            role=CustomUser.TENANT,
            phone_number=None  # No phone number provided
        )
        self.assertIsNone(user_with_no_phone.phone_number)

    def test_string_representation(self):
        """
        Test the string representation of the user.
        """
        self.assertEqual(str(self.user), "testuser")

    def test_role_field_choices(self):
        """
        Test that only the specified role choices are allowed.
        """
        # Test with invalid role
        with self.assertRaises(ValidationError):
            user_with_invalid_role = CustomUser(
                username="invaliduser",
                email="invalid@example.com",
                password="testpass123",
                role="invalidrole"  # Invalid role
            )
            user_with_invalid_role.full_clean()  # This will raise a ValidationError due to invalid role

