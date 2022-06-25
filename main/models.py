from ast import mod
from distutils.command.upload import upload
from email.mime import image
import os
from random import Random
from unicodedata import name
from django.db import models
from location_field.models.plain import PlainLocationField
import uuid
from django.utils.crypto import get_random_string



def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/', filename)
# Create your models here.
class store(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    name = models.CharField(max_length=30)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    data_create=models.DateField()
    capital=models.BigIntegerField()
    purchases=models.BigIntegerField()

    def __str__(self) -> str:
         return self.name
####################################################################
class section(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    name = models.CharField(max_length=30)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)
    image=models.ImageField(upload_to=get_file_path)
    
    def __str__(self) -> str:
        return self.name
####################################################################
class category(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    name = models.CharField(max_length=30)
    section_id = models.ForeignKey('section',on_delete=models.CASCADE)
    image=models.ImageField(upload_to=get_file_path)
   
    
    def __str__(self) -> str:
         return self.name
####################################################################
class product(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    name = models.CharField(max_length=30)
    category_id=models.ForeignKey('category',on_delete=models.CASCADE)
    company_id=models.ForeignKey('company',on_delete=models.CASCADE)
    image=models.ImageField(upload_to=get_file_path)
    unit_name=models.CharField(max_length=50)
    selling_price=models.DecimalField(max_digits=20, decimal_places=10)
    has_list=models.BooleanField(default=False)
    list_name=models.CharField(max_length=50)
    list_amount=models.BigIntegerField()
    listselling_price=models.DecimalField(max_digits=20, decimal_places=10)
    quantityInStore=models.BigIntegerField()
    ReservedQuantitiy=models.IntegerField()   
    
    def __str__(self) -> str:
         return self.name
################################################################
class customer(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    name = models.CharField(max_length=30)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)
    phone=models.CharField(max_length=11)
    image=models.ImageField(upload_to=get_file_path)
    location=PlainLocationField(based_fields=['city'], zoom=7)
    market_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    wallet_money=models.DecimalField(max_digits=20, decimal_places=10)
   
    
    def __str__(self) -> str:
         return self.name
################################################################
class  cart(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    store_id = models.ForeignKey('store',on_delete=models.CASCADE)
    manager_id=models.ForeignKey('customer',on_delete=models.CASCADE)
    date=models.DateField()
    purchas_price=models.DecimalField(max_digits=20, decimal_places=10)


   
    
#################################################################

class  cartitem(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    product_id = models.ForeignKey('product',on_delete=models.CASCADE)
    cart_id=models.ForeignKey('cart',on_delete=models.CASCADE)
    purchas_price=models.FloatField()
    quantity=models.BigIntegerField()
    remaining=models.BigIntegerField()
##################################################################
class  order(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    customer_id=models.ForeignKey('customer',on_delete=models.CASCADE)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('stuff',on_delete=models.CASCADE)
    date=models.DateField()
    purchas_price=models.DecimalField(max_digits=20, decimal_places=10)
    sellin_price=models.DecimalField(max_digits=20, decimal_places=10)
################################################################
class  orderitem(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    order_id=models.ForeignKey('order',on_delete=models.CASCADE)
    product_id=models.ForeignKey('product',on_delete=models.CASCADE)
    selling_price=models.BigIntegerField()
    quantity=models.IntegerField()
    num_list=models.IntegerField()
    list_amount=models.IntegerField()
    list_selling=models.BigIntegerField()
    purchase_price=models.BigIntegerField()
###############################################
class  ads(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    title=models.CharField(max_length=50)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)
#################################################
class month(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)
    date=models.DateField()
    sales_price=models.DecimalField(max_digits=20, decimal_places=10)
    salesPurchasePrice=models.DecimalField(max_digits=20, decimal_places=10)
    expenses=models.DecimalField(max_digits=20, decimal_places=10)
    expensesDescription=models.CharField(max_length=50)
#################################################################
class company(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    name=models.CharField(max_length=50)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)
######################################################################
class stuff(models.Model):
    id = models.CharField(primary_key=True, default= uuid.uuid4, editable=False,max_length=40)
    list=( ('seller','seller'),('employe','employe'),('manager','manager'),('boss','boss') )
    name=models.CharField(max_length=50)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)
    phone=models.CharField(max_length=11)
    image=models.ImageField(upload_to=get_file_path)
    role=models.CharField(max_length=50,choices=list)



   





 
