
from django.urls import URLPattern, path  ,include
from . import views
from django.conf import settings

from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('add',views.add_cart_cartem.as_view(),name="add_cart_cartem"),
    path('get/<str:pk>',views.get_cart_items.as_view(),name="get_cart_cartem"),
    path('store/<str:pk>',views.Get_cart_in_store.as_view(),name="Get_cart_in_store"),
   
   
]