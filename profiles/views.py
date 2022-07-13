import numbers
import random
from django.shortcuts import render
from django.shortcuts import render
from  opt_message.models import opt
from argparse import Action
import imp
from  rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import generics, mixins, viewsets
from rest_framework import request, status, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
import os
from twilio.rest import Client
from rest_framework.authtoken.models import Token
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
                'send' : 'opt-verify'
                }, 
            status=status.HTTP_201_CREATED)
       
    @receiver(post_save, sender=User)
    def send_opt(sender, instance, created, **kwargs):
      if created:
            code=""
            number=instance
            for i in range(0,7):
               n = random.randint(1,9)
               code+=str(n)
            account_sid = 'AC097b5c7e29ab100f96a02bd1028c3d52'
            auth_token =  '79cf2633259a6ed92291e3acb2b6d573'
            client = Client(account_sid, auth_token)
            print(type(instance))
            message = client.messages.create(
                                body= "رمز التاكيد الخاص بيك فى رابح هو "+code,
                                from_='+19794599329',
                                to=number
                            )
           
           
            opt.objects.create(user=instance,opt=code)
           
        


    def list(self, request, *args, **kwargs):
        response = {'message': 'Invild data'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)