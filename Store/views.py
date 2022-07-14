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
class store(viewsets.ModelViewSet):
    queryset = models.store.objects.all()
    serializer_class = serializers.StoreSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class Get_store_name(generics.ListAPIView):
    queryset = models.store.objects.all()
    serializer_class = serializers.StoreName
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    