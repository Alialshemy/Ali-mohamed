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
from location_field.models.plain import PlainLocationField
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.dispatch import receiver
from pkg_resources import require #add this
from Store.models import store
from profiles.models import User_profile
from product.models import product
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/', filename)
# Create your models here.


class  order(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    store_id=models.ForeignKey('Store.store',on_delete=models.CASCADE)
    customer_id=models.ForeignKey('profiles.user_profile',on_delete=models.CASCADE)
    date=models.DateField()
    purchas_price=models.DecimalField(max_digits=20, decimal_places=10)
    profit=models.DecimalField(max_digits=20, decimal_places=10)
    sellin_price=models.DecimalField(max_digits=20, decimal_places=10)
    markert_name=models.CharField(max_length=30)
    customer_name=models.CharField(max_length=30)
    customer_image=models.ImageField(upload_to=get_file_path)
    market_address=models.CharField(max_length=30)
    customer_location=PlainLocationField(based_fields=['city'], zoom=7)
################################################################
class  orderitem(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    order_id=models.ForeignKey('order',on_delete=models.CASCADE)
    product_id=models.ForeignKey('product.product',on_delete=models.CASCADE)
    selling_price=models.DecimalField(max_digits=20, decimal_places=10)
    quantity=models.IntegerField()
    list_amount=models.DecimalField(max_digits=20, decimal_places=10)
    list_selling=models.DecimalField(max_digits=20, decimal_places=10)
    purchase_price=models.DecimalField(max_digits=20, decimal_places=10)
    is_unit=models.BooleanField()
    product_image=models.ImageField(upload_to=get_file_path)
    product_title=models.CharField(max_length=30)
    product_name=models.CharField(max_length=30)
    unit_name=models.CharField(max_length=30)
    list_name=models.CharField(max_length=30)
    total_purchase=models.DecimalField(max_digits=20, decimal_places=10)
    total_selling_price=models.DecimalField(max_digits=20, decimal_places=10)
    profit=models.DecimalField(max_digits=20, decimal_places=10)






 
