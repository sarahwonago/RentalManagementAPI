from rest_framework.permissions import BasePermission


class IsLandLord(BasePermission):
    """
    Custom permission class to allow access to landlord only.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and  request.user.role == "landlord"
    
class IsTenant(BasePermission):
    """
    Custom permission class to allow access to tenants only.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "tenant"