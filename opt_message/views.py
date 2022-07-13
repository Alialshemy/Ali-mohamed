from django.shortcuts import render
import random
from argparse import Action
import imp
from  rest_framework.response import Response

from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, viewsets
from rest_framework import request, status, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from . import models
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
import os
from twilio.rest import Client
from rest_framework.authtoken.models import Token
from . import models
import io
from rest_framework.parsers import JSONParser


####################################################
##############################################
@api_view(['POST'])
def verify(request):
  try:

     otp=request.data[0]["otp"]
     username=request.data[0]["username"]
     print(otp)
     user_id=User.objects.filter(username=username)
     otp_store=models.opt.objects.filter(user=user_id[0].id)
     p=otp_store[0].opt
     if otp == p :
        token, created = Token.objects.get_or_create(user=user_id[0])
        otp_store.delete()
        return Response({ 'token' :token.key })
     else:
         return Response({ "Not Valid otp"})
  except:
     return Response({ "Not Valid Data"})


        
     
'''
class opt(viewsets.ModelViewSet):
    
    account_sid = 'AC097b5c7e29ab100f96a02bd1028c3d52'
    auth_token =  'd49afc7d79f10ec94282579310c01715'
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
                        body=" دذا رمز التاكيد الخاص بيك فى رابح 34342323",
                        from_='+19794599329',
                        to='+201021360285'
                    )

    print(message.sid)
    
'''
