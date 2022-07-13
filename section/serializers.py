from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.section
        fields = '__all__'

