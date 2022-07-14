from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.store
        fields = '__all__'
class StoreName(serializers.ModelSerializer):
    class Meta:
        model = models.store
        fields = ["id","name"]
