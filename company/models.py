from django.db import models
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
# Create your models here.
class  ads(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    title=models.CharField(max_length=50)
    store_id=models.ForeignKey('Store.store',on_delete=models.CASCADE)
#################################################
class month(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    store_id=models.ForeignKey('Store.store',on_delete=models.CASCADE)
    date=models.DateField()
    sales_price=models.DecimalField(max_digits=20, decimal_places=10)
    salesPurchasePrice=models.DecimalField(max_digits=20, decimal_places=10)
    expenses=models.DecimalField(max_digits=20, decimal_places=10)
    expensesDescription=models.CharField(max_length=50)
#################################################################
class company(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    name=models.CharField(max_length=50)
    store_id=models.ForeignKey('Store.store',on_delete=models.CASCADE)