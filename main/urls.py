
from django.urls import path  ,include
from . import api

urlpatterns = [
    path('store/<int:id>', api.get_all_Section_in_store,name='get_all_Section_in_store'),
    path('section/<int:id>', api.get_all_category_in_section,name='get_all_category_in_section'),
    path('category/<int:id>', api.get_all_product_in_category,name='get_all_product_in_category'),
    
]