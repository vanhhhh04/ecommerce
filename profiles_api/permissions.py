from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """check user is trying to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True 
    
        return request.user.id == obj.id
    

class UpdateOwnStatus(permissions.BasePermission):
    """check the user is trying to update their own status"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id 
