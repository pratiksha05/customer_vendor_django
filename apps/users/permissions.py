from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Restrict for Caller Role Users
    """
    message = "You're not authorized to perform this action"

    def has_permission(self, request, view):
        if request.user.role == "ADMIN":
            return True
        return False

