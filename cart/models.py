from ast import mod
import datetime
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
import os
from random import Random
from tkinter.tix import Tree
from turtle import mode
from unicodedata import name
from django.db import models
from location_field.models.plain import PlainLocationField
import uuid
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.dispatch import receiver
from pkg_resources import require #add this
from Store.models import store
from product.models import product
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/', filename)
################################################################
class  cart(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    store_id = models.ForeignKey('Store.store',on_delete=models.CASCADE)
    manager_id=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    total_cost=models.DecimalField(max_digits=20, decimal_places=10)
    cart_number=models.IntegerField()
#################################################################

class  cartitem(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    product_id = models.ForeignKey('product.product',on_delete=models.CASCADE)
    cart_id=models.ForeignKey('cart',on_delete=models.CASCADE)
    purchas_price=models.FloatField()
    quantity=models.BigIntegerField()
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    unitname=models.CharField(max_length=50)
    image=models.ImageField(upload_to=get_file_path)
   




   





 
