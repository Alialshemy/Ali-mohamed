from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.company
        fields = '__all__'
