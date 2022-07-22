import copy
from pyexpat import model
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
from django.core import serializers as ser
from company import models as company_model
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
                    list=[]
                    data={}
                    data_res={}
                    prod=[]
                    star_set = company_model.company.objects.all()
                    for star in star_set.iterator():
                        if  product_model.product.objects.filter(company_id=star.id,category_id=pk)  :
                                
                                instance= ser.serialize("python",product_model.product.objects.filter(company_id=star.id))
                                for items in instance :
                                
                                    prod.append(items['fields'])
                                data['name']=star.name
                                data['Product']=copy.deepcopy(prod)
                                prod.clear()
                                data_res[star.id]=copy.deepcopy(data)
                            # data.clear()
                    list.append(data_res)
                    return Response (list)
            except:
                return Response ({"Error"})
                    