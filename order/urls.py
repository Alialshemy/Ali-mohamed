
from django.urls import URLPattern, path  ,include
from . import views
from django.conf import settings

from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
#router.register('register', api.UserViewSet)
router.register('order',views.order )
router.register('orderitems',views.orderitems )


urlpatterns = [
    
    path('', include(router.urls)),
    path('add',views.Add_order.as_view())
   
]