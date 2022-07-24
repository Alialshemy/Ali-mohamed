import copy
from pyexpat import model
from tkinter.tix import Tree
from django.shortcuts import render


from argparse import Action
import imp
from  rest_framework.response import Response

from cart.models import cartitem
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
from django.core import serializers as ser
from company import models as company_model
from product import serializers as product_serialzer
from rest_framework.authtoken.models import Token
############################################################
class category(viewsets.ModelViewSet):
    queryset = models.category.objects.all()
    serializer_class = serializers.CategorySerializer
 #   authentication_classes = (TokenAuthentication,)
 #   permission_classes = (IsAuthenticated,)
   
class Get_Product_in_Category(views.APIView):
    #  authentication_classes = (TokenAuthentication,)
    #  permission_classes = (IsAuthenticated,)
      def get(self, request, pk):
        #   product_data=product_model.product.objects.filter(category_id=pk)
         #  if product_data :
         #        data=product_serialzer.ProductSerializer(product_data,many=True)
         #        return Response (data.data)
        #   else:
        #        return Response ({"Not Found any product"})
            try:
                   
                    data_res={}
                    star_set = company_model.company.objects.all()
                    for star in star_set.iterator():                        
                        if  product_model.product.objects.filter(company_id=star.id,category_id=pk)  :
                               
                                instance=product_serialzer.ProductSerializer(product_model.product.objects.filter(company_id=star.id,category_id=pk),many=True).data

                                data_res[star.name]=instance
                    return Response (data_res)
            except:
                return Response ({"Error"})
