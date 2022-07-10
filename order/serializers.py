from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.order
        fields = '__all__'
class OrderitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.orderitem
        fields = '__all__'