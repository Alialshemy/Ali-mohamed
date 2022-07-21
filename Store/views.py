from django.shortcuts import render


from argparse import Action
import imp
from  rest_framework.response import Response

from section.models import section
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, viewsets,views
from rest_framework import request, status, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from section import models as section_model
from section import serializers as sections_ser
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.authtoken.models import Token
#####################################################
class store(viewsets.ModelViewSet):
    queryset = models.store.objects.all()
    serializer_class = serializers.StoreSerializer
  #  authentication_classes = (TokenAuthentication,)
 #   permission_classes = (IsAuthenticated,)

class Get_store_name(generics.ListAPIView):
    queryset = models.store.objects.all()
    serializer_class = serializers.StoreName
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
class Get_Section_in_store(views.APIView):
      authentication_classes = (TokenAuthentication,)
      permission_classes = (IsAuthenticated,)
      def get(self, request, pk):
           section_data=section_model.section.objects.filter(store_id=pk)
           if section_data :
                 data=sections_ser.SectionSerializer(section_data,many=True)
                 return Response (data.data)
           else:
                return Response ({"Not Found any Section"})
