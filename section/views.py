from unicodedata import category
from django.shortcuts import render


from argparse import Action
import imp
from  rest_framework.response import Response

from Store import views
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, viewsets
from rest_framework import request, status, viewsets,views
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from Category import models as model_categ
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.core import serializers as ser
from rest_framework.authtoken.models import Token
from Category import serializers as category_serialzer
#############################################################
class sections(viewsets.ModelViewSet):
    queryset = models.section.objects.all()
    serializer_class = serializers.SectionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
############################################################
class Get_category_in_section(views.APIView):
      authentication_classes = (TokenAuthentication,)
      permission_classes = (IsAuthenticated,)
      def get(self, request, pk):
           categorys=model_categ.category.objects.filter(section_id=pk)
           if categorys :
                 data=category_serialzer.CategorySerializer(categorys,many=True)
                 return Response (data.data)
           else:
                return Response ({"Not Found any category"})
