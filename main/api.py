
from  rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, viewsets
#####################################################
class get_all_Section_in_store(generics.ListAPIView):
    queryset = models.section.objects.all()
    serializer_class = serializers.SectionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

#############################################################
class get_all_category_in_section(generics.ListAPIView):
    queryset = models.category.objects.filter(section_id=id)
    serializer_class = serializers.SectionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
############################################################
class get_all_product_in_category(generics.ListAPIView):
    queryset = models.product.objects.filter(category_id=id)
    serializer_class = serializers.SectionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
###################################################################