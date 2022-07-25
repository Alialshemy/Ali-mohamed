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
   
class Get_product(views.APIView):
    def get(self,request,pk):
        prod=models.product.objects.filter(id=pk)
        data=serializers.ProductSerializer(prod,many=True).data
        return Response(data)
