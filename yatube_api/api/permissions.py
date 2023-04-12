from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'Нельзя редактировать чужое сообщение'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
