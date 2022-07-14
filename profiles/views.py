from asyncio import FastChildWatcher
from lib2to3.pgen2 import token
import numbers
import random
from django.shortcuts import render
from django.shortcuts import render
from  opt_message import  models as otp
from argparse import Action
import imp
from  rest_framework.response import Response
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
from rest_framework.decorators import api_view
from . import models
# Create your views here.

def check_user_exit(username):
    
     try:
        user_Exit=False
        otp.otp.objects.get(username=username)
        return True
     except otp.otp.DoesNotExist:
         return False
   
class Profile(generics.CreateAPIView):
    queryset = models.profile.objects.all()
    serializer_class = serializers.ProfileSerialzer
  #  authentication_classes = (TokenAuthentication,)
  #  permission_classes = (IsAuthenticated,)



@api_view(['POST'])
def register(request):
    
   try:
     
     username=request.data.get("username")
     password=request.data.get("password")
     if not check_user_exit(username):            
            code=send_opt(username)     
            otp.otp.objects.create(username=username,password=password,otp=code)
            return Response({ "send":"OK"})

     else:
        return Response({ "send":"user Exit"})
    
   except: 
    return Response({ "ERROR Data"})
#######################################################
def send_opt(username):
        
        try:
                    code=""
                    number=username
                    for i in range(0,7):
                                n = random.randint(1,9)
                                code+=str(n)
                    account_sid = 'AC097b5c7e29ab100f96a02bd1028c3d52'
                    auth_token =  '3b52d463a7784de749e2de88c55634ec'
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                                        body= "رمز التاكيد الخاص بيك فى رابح هو "+code,
                                        from_='+19794599329',
                                        to=number
                                    )
                    return code 
            
        except:
            return "error"
                
@api_view(['POST'])
def login(request):
  try:
     
     username=request.data.get("username")
     password=request.data.get("password")
     user=User.objects.get(username=username)
     if user.check_password(password):
           otp=Token.objects.get(user=user.id)
           return Response({ 'token':otp.key})
     else:
          return Response({ 'user' :"password Error"})       
     
    
  except:
     return Response({ "Not Register"})