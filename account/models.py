import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model.

    with added id and role attributes.
    """
    ROLE_CHOICES = (
        ("landlord", "landlord"),
        ("tenant", "tenant"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="tenant")

    def __str__(self):
        return self.username