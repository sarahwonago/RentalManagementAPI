
import uuid
from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Tenant(models.Model):
    """
    Model for linking tenants to landlords.
    """
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
        )

    # a tenant can only be linked to one landlord
    tenant = models.OneToOneField(User, on_delete=models.CASCADE)

    # a landlord can be linked to more than one tenant
    landlord = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="landlordtenants"
        )
    
    # house one to one
    # due_date for rent payment on the house
     
    
    def __str__(self):
        return f"{self.tenant.username} - Rents at {self.landlord.username}"