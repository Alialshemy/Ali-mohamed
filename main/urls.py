
from django.urls import URLPattern, path  ,include
from . import api
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('store/<str:id>', api.get_all_Section_in_store,name='get_all_Section_in_store'),
    path('section/<str:id>', api.get_all_category_in_section,name='get_all_category_in_section'),
    path('category/<str:id>', api.get_all_product_in_category,name='get_all_product_in_category'),
    
]