import copy
import json
from urllib import response
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
from company.models  import company
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.core import serializers as ser
from rest_framework.authtoken.models import Token
###################################################################
class product_add(generics.CreateAPIView):
    queryset = models.product.objects.all()
    serializer_class = serializers.ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
   
   
   
class Get_product (views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        try:
                data={}
                data_res={}
                prod=[]
                star_set = models.company.objects.all()
                for star in star_set.iterator():
                    
                    if  models.product.objects.filter(company_id=star.id):
                            
                            instance= ser.serialize("python",models.product.objects.filter(company_id=star.id))
                            for items in instance :
                            
                                prod.append(items['fields'])
                            data['name']=star.name
                            data['Product']=copy.deepcopy(prod)
                            prod.clear()
                            data_res[star.id]=copy.deepcopy(data)
                        # data.clear()
            
                return Response (data_res)
        except:
             return Response ({"Error"})

