from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


from . import models
from . import serializers
from . import permissions

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateProfilePermission,)



class TodoStuffViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.TodoStuffSerializer
    queryset = models.TodoStuffs.objects.all()

    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthenticated, permissions.AddTodoStuffPermission, ]

    
    def get_queryset(self):

        user = self.request.user
        return models.TodoStuffs.objects.filter(user=user)

        

    def perform_create(self, serializer):

        serializer.save(user=self.request.user) 

