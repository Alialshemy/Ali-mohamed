
from argparse import Action
import imp
from  rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, viewsets
from rest_framework import request, status, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
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
    @action(detail=True,methods=['get'],url_path='store')
    def section_in_store(self,request,pk=None):
        st=models.section.objects.filter(store_id=pk)
        serializer = self.get_serializer(st,many=True)
        return Response (serializer.data)
  #  authentication_classes = (TokenAuthentication,)
  #  permission_classes = (IsAuthenticated,)
############################################################
class category(viewsets.ModelViewSet):
    queryset = models.category.objects.all()
    serializer_class = serializers.CategorySerializer
    # authentication_classes = (TokenAuthentication,)
  #  permission_classes = (IsAuthenticated,)
    @action(detail=True,methods=['get'],url_path='section')
    def cartegory_in_section(self,request,pk=None):
        st=models.category.objects.filter(section_id=pk)
        serializer = self.get_serializer(st,many=True)
        return Response (serializer.data)

###################################################################
class product(viewsets.ModelViewSet):
    queryset = models.product.objects.all()
    serializer_class = serializers.ProductSerializer
    # authentication_classes = (TokenAuthentication,)
  #  permission_classes = (IsAuthenticated,)
    @action(detail=True,methods=['get'],url_path='category')
    def product_in_category(self,request,pk=None):
        st=models.product.objects.filter(category_id=pk)
        serializer = self.get_serializer(st,many=True)
        return Response (serializer.data)
##############################################
class cart(viewsets.ModelViewSet):
    queryset = models.cart.objects.all()
    serializer_class = serializers.ProductSerializer
    # authentication_classes = (TokenAuthentication,)
  #  permission_classes = (IsAuthenticated,)
class cartitems(viewsets.ModelViewSet):
    queryset = models.cartitem.objects.all()
    serializer_class = serializers.ProductSerializer
    # authentication_classes = (TokenAuthentication,)
  #  permission_classes = (IsAuthenticated,)
   
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