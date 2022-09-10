from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticated Users only can see ListView
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # read permission allowed to any request
        # GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # But, Only author can edit or delete it
        return obj.author == request.user
