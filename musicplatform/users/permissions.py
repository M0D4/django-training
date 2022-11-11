from rest_framework import permissions


class IsSameUser(permissions.BasePermission):
    def has_object_permission(self, request, view, user):
        return request.method in permissions.SAFE_METHODS or user.id == request.user.id
