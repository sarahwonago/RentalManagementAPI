
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

    # Tenant must be a user with the role 'tenant'
    tenant = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'tenant'}, related_name='tenant')

    # a landlord can be linked to more than one tenant
    # Landlord must be a user with the role 'landlord'
    landlord = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'landlord'}, 
        related_name='tenants'
        )
    
    # house one to one
    # due_date for rent payment on the house
     
    
    def __str__(self):
        return f"{self.tenant.username} - Rents at {self.landlord.username}"


