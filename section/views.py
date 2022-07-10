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
#############################################################
class sections(viewsets.ModelViewSet):
    queryset = models.section.objects.all()
    serializer_class = serializers.SectionSerializer
    @action(detail=True,methods=['get'],url_path='store')
    def section_in_store(self,request,pk=None):
        st=models.section.objects.filter(store_id=pk)
        serializer = self.get_serializer(st,many=True)
        return Response (serializer.data)
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
############################################################