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
from Store.models import store
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.dispatch import receiver
from pkg_resources import require #add this
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/', filename)
# Create your models here.
class section(models.Model):
    
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    name = models.CharField(max_length=30)
    store_id=models.ForeignKey('Store.store',on_delete=models.CASCADE)
    image=models.ImageField(upload_to=get_file_path)
    
    def __str__(self) -> str:
        return self.name