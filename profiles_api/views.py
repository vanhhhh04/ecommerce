from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import permissions
from profiles_api import serializers
from profiles_api.models import UserProfile,ProfileFeedItem

# Create your views here.


class HelloAPI(APIView):
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        an_apiview = ['hello world']
        return Response({'message':an_apiview})
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'

            return Response({'message':message})

        else :
            return Response(status=status.HTTP_400_BAD_REQUEST) 

    def put(self, request, pk=None):
        return Response({'method':'PUT'})
    

    def patch(self, request, pk=None):
        return Response({'method':'patch'})
    

    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    
    def list(self,request):
        an_viewset = ['hello world viewset']
        return Response({'message':an_viewset})
    
    def create(self,request):
        pass


    def retrieve(self,request):
        pass 


    def update(self,request):
        pass 


    def partial_update(self,request):
        pass 

    
    def destroy(self,request,pk=None):
        pass


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfile
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly,
    )


    def perform_create(self,serializer):
        serializer.save(user_profile=self.request.user)




