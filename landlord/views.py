from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from account.permissions import IsLandLord
from account.serializers import UserSerializer

from tenant.serializers import TenantRegistrationSerializer
from tenant.models import Tenant

from django.contrib.auth import get_user_model

User = get_user_model()
