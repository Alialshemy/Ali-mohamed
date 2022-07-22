
from django.urls import URLPattern, path  ,include
from . import views
from django.conf import settings

from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
#router.register('register', api.UserViewSet)

router.register('',views.category )
urlpatterns = [
  #  path('store/<str:id>', api.get_all_Section_in_store.as_view(),name='get_all_Section_in_store'),
 #   path('section/<str:id>', api.get_all_category_in_section.as_view(),name='get_all_category_in_section'),
#    path('category/<str:id>', api.get_all_product_in_category.as_view(),name='get_all_product_in_category'),
    # create token 
    
     path('get/product/<str:pk>',views.Get_Product_in_Category.as_view(),name='Get_Product_in_Category'),
    path('', include(router.urls)),
]