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
from Category.models import category
from company.models import company
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/', filename)
# Create your models here.

class product(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    name = models.CharField(max_length=30)
    category_id=models.ForeignKey('Category.category',on_delete=models.CASCADE)
    company_id=models.ForeignKey('company.company',on_delete=models.CASCADE)
    image=models.ImageField(upload_to=get_file_path)
    unit_name=models.CharField(max_length=50)
    selling_price=models.DecimalField(max_digits=20, decimal_places=10)
    has_list=models.BooleanField()
    list_name=models.CharField(max_length=50)
    list_amount=models.BigIntegerField()
    listselling_price=models.DecimalField(max_digits=20, decimal_places=10)
    quantityInStore=models.BigIntegerField()
    title=models.CharField(max_length=30)
    purchase_price=models.DecimalField(max_digits=50,decimal_places=10)
    purchase_cost=models.DecimalField(max_digits=50,decimal_places=10)
    def __str__(self) -> str:
         return self.name
################################################################


   





 
