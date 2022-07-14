from django.contrib.auth.models import User, Group
from rest_framework import serializers
from opt_message import models as opt
from . import models
class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = opt.otp
        fields = '__all__'
class ProfileSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.profile
        fields = '__all__'

