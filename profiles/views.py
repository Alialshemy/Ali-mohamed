from asyncio import FastChildWatcher
from lib2to3.pgen2 import token
import numbers
from operator import eq
import random
import re
from django.shortcuts import render
from django.shortcuts import render
from  opt_message import  models as otp
from argparse import Action
import imp
from  rest_framework.response import Response
from . import serializers
from rest_framework import generics, mixins, viewsets
from rest_framework import request, status, viewsets,views
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
   # create new profile with user
class Profile(generics.CreateAPIView):
    queryset = models.User_profile.objects.all()
    serializer_class = serializers.ProfileSerialzer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
# return user with specific Role
class Show_Custom_user(views.APIView):
   authentication_classes = (TokenAuthentication,)
   permission_classes = (IsAuthenticated,)
   def get(self, request, role):
      try:
        data = models.User_profile.objects.filter(Role=role)
        if data:
            serializer = serializers.ShowCustomSerialzer(data, many=True)
            return Response(status=200, data=serializer.data)
        return Response(status=400, data={"User not found"})
      except:
         return Response(status=400, data={"Error"})
###################################################################
# Return profile with specifi user         
class Get_profile(views.APIView):
   authentication_classes = (TokenAuthentication,)
   permission_classes = (IsAuthenticated,)
   def get(self, request, id):
      try:
        data = models.User_profile.objects.filter(user_id=id)
        if data:
            serializer = serializers.ProfileSerialzer(data, many=True)
            return Response(status=200, data=serializer.data)
        return Response(status=400, data={"profile not found"})
      except:
            return Response(status=400, data={"Not valid Id"})
################################################################################
#  change role to specific user the do by boss only
class Change_role(views.APIView):

    def post(self, request):
      try:
            data = serializers.ChangeRoleSerialzer(request.data)
            if request.data['Role'] == "customer" or request.data['Role'] == "manager" or request.data['Role'] == "stuff" or request.data['Role'] == "seller":
                  change_user= models.User_profile.objects.filter(id=request.data['id']).update(Role=request.data['Role'])
            else:
               return Response(status=400, data={"Not valid Role"})
            return Response(status=200, data={"Chane Success"})
      except:
           return Response(status=200, data={"Not valid data"})
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
                    auth_token =  'b9cbeb02b552d2e3b2484be826347cbc'
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                                        body= "رمز التاكيد الخاص بيك فى رابح هو "+code,
                                        from_='+19794599329',
                                        to=number
                                    )
                    return code 
            
        except:
            return "error"

########################################################


@api_view(['POST'])
def login(request):
 # try:
     
            username=request.data.get("username")
            password=request.data.get("password")
            
            if True:
                  user=User.objects.get(username=username)
                  if user.check_password(password):
                        otp=Token.objects.get(user=user.id)
                        ali=profile=models.User_profile.objects.get(user_id=user.id)
                        store_id=ali.store_id
                        return Response({ 'token':otp.key,'user_id':user.id, 'store_id': str(store_id)})
                  else:
                            return Response({ 'user' :"password Error"})       
            
            else :
                  return Response({ 'Error' :"Invalid number "}) 
 # except:
#     return Response({ "Not Register"})