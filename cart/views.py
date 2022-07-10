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
#####################################################

class cart(viewsets.ModelViewSet):
    queryset = models.cart.objects.all()
    serializer_class = serializers.CartSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
class cartitems(viewsets.ModelViewSet):
    queryset = models.cartitem.objects.all()
    serializer_class = serializers.CartItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
  #######################################################
