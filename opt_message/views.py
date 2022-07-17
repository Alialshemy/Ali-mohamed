from email import message
from django.shortcuts import render
import random
from argparse import Action
import imp
from  rest_framework.response import Response

from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, viewsets ,views
from rest_framework import request, status, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from . import models
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
import os
from twilio.rest import Client
from rest_framework.authtoken.models import Token
import io
from rest_framework.parsers import JSONParser


####################################################
##############################################
@api_view(['POST'])
def verify(request):
  try:

     otp=request.data.get('otp')
     username=request.data.get('username')
     otp_store=models.otp.objects.filter(username=username)
     p=otp_store[0].otp
     if otp == p :
        cuser=User.objects.create(username=otp_store[0].username)
        cuser.set_password(otp_store[0].password)
        cuser.save()
        token, created = Token.objects.get_or_create(user=cuser)
        otp_store.delete()
        return Response({ 'token' :token.key ,"user_id":cuser.id})
     else:
         return Response({ "Not Valid otp"})
  except:
     return Response({ "Not Valid Data"})

class Send_messages_to_user(views.APIView):
    def post(self, request):
        data=request.data
        messag_send=data[0]['message']
        users=data[0]['user']
        for user in users:

            send_messages(user['phone'],messag_send)
        return Response({ 'send':'ok'})

def send_messages(phone,message):
      try:
            print (message,phone)
            account_sid = 'AC097b5c7e29ab100f96a02bd1028c3d52'
            auth_token =  'b9cbeb02b552d2e3b2484be826347cbc'
            client = Client(account_sid, auth_token)
            
            message = client.messages.create(
                                body=message,
                                from_='+19794599329',
                                to=phone
                           )
      except:
          return "Erorr to send message "

    
    

    

        
     
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
