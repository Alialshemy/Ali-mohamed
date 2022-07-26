from django.shortcuts import render


from argparse import Action
import imp
from  rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, viewsets ,request, status,views 
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.authtoken.models import Token
####################################################
##############################################
class order(viewsets.ModelViewSet):
    queryset = models.order.objects.all()
    serializer_class = serializers.OrderSerializer
 #   authentication_classes = (TokenAuthentication,)
 #   permission_classes = (IsAuthenticated,)
   #################################################
class orderitems(viewsets.ModelViewSet):
    queryset = models.orderitem.objects.all()
    serializer_class = serializers.OrderitemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class Add_order(views.APIView):
    def post(self,request):
        data=request.data
        orderitems=data['orderitems']
      

