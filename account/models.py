import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model with roles for landlord and tenant.

    Additional fields:
        phone_number: Phone number of the user.
    """
    LANDLORD = "landlord"
    TENANT = "tenant"
    DEFAULT = "user"
    
    ROLE_CHOICES = (
        ("landlord", "landlord"),
        ("tenant", "tenant"),
        ("user", "user"),
        
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default="user",
        help_text="Role either: 'user','landlord' or 'tenant'."
        )

    def __str__(self):
        return self.username