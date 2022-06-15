
from  rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.decorators import api_view
#####################################################
@api_view(['GET'])
def get_all_Section_in_store(request,id):
    sections= models.section.objects.all()
    data=serializers.SectionSerializer(sections,many=True).data
    return Response({'data':data})
#############################################################
@api_view(['GET'])
def get_all_category_in_section(request,id):
    category= models.category.objects.filter(section_id=id)
    data=serializers.CategorySerializer(category,many=True).data
    return Response({'data':data})
############################################################
@api_view(['GET'])
def get_all_product_in_category(request,id):
    product= models.product.objects.filter(category_id=id)
    data=serializers.ProductSerializer(product,many=True).data
    return Response({'data':data})