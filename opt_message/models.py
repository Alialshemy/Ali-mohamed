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
# Create your models here.
class otp(models.Model):
    otp=models.CharField(max_length=10)
    username = models.CharField(max_length=12)
    password=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.otp