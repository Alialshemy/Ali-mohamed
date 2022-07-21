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
        model = models.User_profile
        fields = '__all__'
class ChangeRoleSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.User_profile
        fields = ['id','Role']
class ShowCustomSerialzer(serializers.ModelSerializer):
   # user_id=
    class Meta:
        model = models.User_profile
        fields = ['id','user_id','name','market_name','image']
