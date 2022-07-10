from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.cart
        fields = '__all__'
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.cartitem
        fields = '__all__'
