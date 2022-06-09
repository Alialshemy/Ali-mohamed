
from django.urls import path  ,include
from . import api

urlpatterns = [
   
    path('list/', api.customerapi,name='customerapi'),
]