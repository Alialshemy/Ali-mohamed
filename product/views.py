from django.shortcuts import render


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

