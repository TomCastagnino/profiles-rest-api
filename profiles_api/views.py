from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers, models, permissions



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
