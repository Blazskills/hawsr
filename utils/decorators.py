from rest_framework import permissions
from utils.api_exceptions import (
    InactiveUserException,
    NotAdminException,
)


class DisallowedUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_active:
            raise InactiveUserException
        return True


class DisallowedNotAdminManagementPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        if request.user.get_role_display() != "Admin":
            raise NotAdminException
        return True
