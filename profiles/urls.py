
from django.urls import URLPattern, path  ,include
from . import views
from django.conf import settings

from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
#router.register('register', api.UserViewSet)
#router.register('register',views.UserViewSet )



urlpatterns = [
  #  path('store/<str:id>', api.get_all_Section_in_store.as_view(),name='get_all_Section_in_store'),
 #   path('section/<str:id>', api.get_all_category_in_section.as_view(),name='get_all_category_in_section'),
#    path('category/<str:id>', api.get_all_product_in_category.as_view(),name='get_all_product_in_category'),
    # create token 
    path('register', views.register,name='register'),
    path('login',views.login,name='login'),
    path('createprofile',views.Profile.as_view(),name='login'),
    path('get/<str:role>',views.Show_Custom_user.as_view(),name='Show_user'),
    path('role',views.Change_role.as_view(),name='Change_role'),
     path('profile/<int:id>',views.Get_profile.as_view(),name='Show_profile'),



   
]