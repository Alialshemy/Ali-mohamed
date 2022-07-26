from statistics import mode
from tkinter.tix import Tree
from typing import List
from django.dispatch import receiver
from django.shortcuts import render


from argparse import Action
import imp
from  rest_framework.response import Response
from django.db.models.signals import post_save

from Category import views
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, viewsets,views
from rest_framework import request, status, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from . import models
from product import models as product_model
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from Store import models as store_model
from rest_framework.authtoken.models import Token
#####################################################

  #get cart and items in this cart 
class get_cart_items(views.APIView):
  # authentication_classes = (TokenAuthentication,)
  # permission_classes = (IsAuthenticated,)
   def get(self,request,pk):
      try:
                   
                    data={}
                    cart = models.cart.objects.get(id=pk) 
                   
                    cart_data=serializers.CartSerializer(cart)
                    data=cart_data.data
                    items=models.cartitem.objects.filter(cart_id=pk)   
                 
                    items_data=serializers.CartItemSerializer(items,many=True)
                    data['items']=items_data.data  
                    return Response (data)
      except:
            return Response ({"invalid pk"})
#add cart and cart items 
class add_cart_cartem(views.APIView):
   # authentication_classes = (TokenAuthentication,)
   # permission_classes = (IsAuthenticated,)
    def post(self,request):
       try:   
            data=request.data
            cartitem=request.data.get('items')
            number_cart=(models.cart.objects.filter(store_id=data['store_id']).count())+1
            print(number_cart)
            cart_obg=models.cart.objects.create(store_id=store_model.store.objects.get(id=data['store_id']),manager_id=User.objects.get(id=data['manager_id']),total_cost=data['total_cost'],cart_number=number_cart)
            for item in cartitem:
                  if cart_obg:
                        models.cartitem.objects.create(
                          product_id=product_model.product.objects.get(id=item['product_id']),
                          cart_id=cart_obg,
                          purchas_price=item['purchas_price'],
                          quantity=item['quantity'],
                          name=item['name'],
                          title=item['title'],
                          unitname=item['unitname'],
                          image=item['image']

                          ) 
            return Response({"ok"}, status=status.HTTP_200_OK) 
       except:
         return Response({"Invalid data"}, status=status.HTTP_400_BAD_REQUEST) 
# Get all cart in store
class Get_cart_in_store(views.APIView):
  def get(self,request,pk):
       data=models.cart.objects.filter(store_id=pk).order_by('cart_number').reverse()
       return Response (serializers.CartSerializer(data,many=True).data)
@receiver(post_save, sender=models.cartitem)
def update_field(sender, instance, **kwargs):
   try:
      product=instance.product_id
      product.quantityInStore=product.quantityInStore+instance.quantity
      product.purchase_cost = float(product.purchase_cost) + ( float( instance.purchas_price) * float( instance.quantity))
      product.purchase_price= product.purchase_cost / product.quantityInStore
      product.save()
      print("sffdsfdsdf")
   except:
    print ("error signal") 
  