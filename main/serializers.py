from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.section
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.category
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.product
        fields = '__all__'

