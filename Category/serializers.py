from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.category
        fields = '__all__'
