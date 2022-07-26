from django.contrib.auth.models import User, Group
from rest_framework import serializers
from section import models as sec_model
from . import models
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.store
        fields = '__all__'
class StoreName(serializers.ModelSerializer):
    class Meta:
        model = models.store
        fields = ["id","name"]


