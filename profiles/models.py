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
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/', filename)
###############################
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_id=models.ForeignKey('Store.store',on_delete=models.CASCADE,default="null")
    phone=models.CharField(max_length=11,default='00000000000')
    image=models.ImageField(upload_to=get_file_path)
    location=PlainLocationField(based_fields=['city'], zoom=7)
    market_name=models.CharField(max_length=50,default='null')
    address=models.CharField(max_length=50,default='null')
    wallet_money=models.DecimalField(max_digits=20, decimal_places=10,default=0)    
    def __str__(self):
        return self.user.username
class stuff(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    list=( ('seller','seller'),('employe','employe'),('manager','manager'),('boss','boss') )
    name=models.CharField(max_length=50)
    store_id=models.ForeignKey('Store.store',on_delete=models.CASCADE)
    phone=models.CharField(max_length=11)
    image=models.ImageField(upload_to=get_file_path)
    role=models.CharField(max_length=50,choices=list)




   





 