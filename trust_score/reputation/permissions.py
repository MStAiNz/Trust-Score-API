from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsReputationAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='ReputationAdmins').exists()