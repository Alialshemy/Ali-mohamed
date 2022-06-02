from django.db import models

# Create your models here.
class store(models.Model):
    name = models.CharField(max_length=30)
    generalmanageid = models.ForeignKey('general_manager',on_delete=models.CASCADE)
    def __str__(self) -> str:
         return self.name
class section(models.Model):
    name = models.CharField(max_length=30)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)
   
    
    def __str__(self) -> str:
        return self.name
class category(models.Model):
    name = models.CharField(max_length=30)
    section_id = models.ForeignKey('section',on_delete=models.CASCADE)
   
    
    def __str__(self) -> str:
         return self.name
class product(models.Model):
    name = models.CharField(max_length=30)
    category_id=models.ForeignKey('category',on_delete=models.CASCADE)
   
    
    def __str__(self) -> str:
         return self.name
class customer(models.Model):
    name = models.CharField(max_length=30)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)
   
    
    def __str__(self) -> str:
         return self.name
class  general_manager(models.Model):
    name = models.CharField(max_length=30)
   
    
    def __str__(self) -> str:
         return self.name
class  manager(models.Model):
    name = models.CharField(max_length=30)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)

   
    
    def __str__(self) -> str:
         return self.name
class  cart(models.Model):
    store_id = models.ForeignKey('store',on_delete=models.CASCADE)
    manager_id=models.ForeignKey('manager',on_delete=models.CASCADE)


   
    
   

class  cartitem(models.Model):
    product_id = models.ForeignKey('product',on_delete=models.CASCADE)
    cart_id=models.ForeignKey('cart',on_delete=models.CASCADE)

class  stuff(models.Model):
    name = models.CharField(max_length=30)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)
    
    def __str__(self) -> str:
         return self.name
class  seller(models.Model):
    name = models.CharField(max_length=30)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)
   
    
    def __str__(self) -> str:
         return self.name
class  order(models.Model):
    customer_id=models.ForeignKey('customer',on_delete=models.CASCADE)
    store_id=models.ForeignKey('store',on_delete=models.CASCADE)
    seller_id=models.ForeignKey('seller',on_delete=models.CASCADE)
class  orderitem(models.Model):
    order_id=models.ForeignKey('order',on_delete=models.CASCADE)
    product_id=models.ForeignKey('product',on_delete=models.CASCADE)
   





 
