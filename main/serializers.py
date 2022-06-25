from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.section
        fields = '__all__'
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.store
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.category
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.product
        fields = '__all__'
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.cart
        fields = '__all__'
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.cartitem
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
