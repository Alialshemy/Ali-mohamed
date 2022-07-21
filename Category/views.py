from django.shortcuts import render


from argparse import Action
import imp
from  rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, viewsets,views
from rest_framework import request, status, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from  product import models as product_model 
from   product import serializers as product_serialzer
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.authtoken.models import Token
############################################################
class category(viewsets.ModelViewSet):
    queryset = models.category.objects.all()
    serializer_class = serializers.CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
   
class Get_Product_in_Category(views.APIView):
    #  authentication_classes = (TokenAuthentication,)
    #  permission_classes = (IsAuthenticated,)
      def get(self, request, pk):
           product_data=product_model.product.objects.filter(category_id=pk)
           if product_data :
                 data=product_serialzer.ProductSerializer(product_data,many=True)
                 return Response (data.data)
           else:
                return Response ({"Not Found any product"})