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
class product(viewsets.ModelViewSet):
    queryset = models.product.objects.all()
    serializer_class = serializers.ProductSerializer
   # authentication_classes = (TokenAuthentication,)
 #   permission_classes = (IsAuthenticated,)
    def list(self, request, *args, **kwargs):
        queryset=models.product.objects.all().order_by('company_id')
        serializer =serializers.ProductSerializer(queryset,many=True)
        print(type(serializer))
        serializer.insert()
        return Response(serializer.data)
    @action(detail=True,methods=['get'],url_path='category')
    def product_in_category(self,request,pk=None):
        st=models.product.objects.filter(category_id=pk)
        serializer = self.get_serializer(st,many=True)
        return Response (serializer.data)
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
                            
                        
                            
              #  print(data)  
            #  app_json = json.dumps(data, sort_keys=True)
            #  print(app_json)
            
                return Response (data_res)
        except:
             return Response ({"Error"})

