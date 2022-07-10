from ast import mod
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
import os
from random import Random
from tkinter.tix import Tree
from unicodedata import name
from django.db import models
from location_field.models.plain import PlainLocationField
import uuid
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.dispatch import receiver
from pkg_resources import require #add this
from Store.models import store
from profiles.models import stuff
from product.models import product
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/', filename)
# Create your models here.


class  order(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    store_id=models.ForeignKey('Store.store',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('profiles.stuff',on_delete=models.CASCADE)
    date=models.DateField()
    purchas_price=models.DecimalField(max_digits=20, decimal_places=10)
    sellin_price=models.DecimalField(max_digits=20, decimal_places=10)
################################################################
class  orderitem(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    order_id=models.ForeignKey('order',on_delete=models.CASCADE)
    product_id=models.ForeignKey('product.product',on_delete=models.CASCADE)
    selling_price=models.BigIntegerField()
    quantity=models.IntegerField()
    num_list=models.IntegerField()
    list_amount=models.IntegerField()
    list_selling=models.BigIntegerField()
    purchase_price=models.BigIntegerField()






 
