from django.contrib.auth.models import User, Group
from rest_framework import serializers
from opt_message import models
class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.otp
        fields = '__all__'

