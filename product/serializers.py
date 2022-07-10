from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.product
        fields = '__all__'
