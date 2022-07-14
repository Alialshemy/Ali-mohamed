from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models

class OptSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.otp
        fields = '__all__'
class verify:
    def __init__(self, opt, id):
        self.opt = opt
        self.id = id

class verifySerliazer(serializers.Serializer):
    id = serializers.CharField(max_length=20)
    opt = serializers.CharField(max_length=20)