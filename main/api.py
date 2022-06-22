
from  rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, viewsets
from rest_framework import request, status, viewsets
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.authtoken.models import Token
#####################################################
class store(viewsets.ModelViewSet):
    queryset = models.store.objects.all()
    serializer_class = serializers.StoreSerializer
   # authentication_classes = (TokenAuthentication,)
   # permission_classes = (IsAuthenticated,)
   

#############################################################
class sections(viewsets.ModelViewSet):
    queryset = models.section.objects.all()
    serializer_class = serializers.SectionSerializer
  #  authentication_classes = (TokenAuthentication,)
  #  permission_classes = (IsAuthenticated,)
############################################################
class category(viewsets.ModelViewSet):
    queryset = models.category.objects.all()
    serializer_class = serializers.CategorySerializer
  #  authentication_classes = (TokenAuthentication,)
  #  permission_classes = (IsAuthenticated,)

###################################################################
'''
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    #authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({
                'token': token.key, 
                }, 
            status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        response = {'message': 'Invild data'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
        '''