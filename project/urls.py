"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import statistics
from django.conf import settings
from django.contrib import admin
from django.urls import path  ,include
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('product/', include('product.urls')),
    path('', include('cart.urls')),
    path('', include('order.urls')),
    path('store/', include('Store.urls')),
    path('section/', include('section.urls')),
    path('category/', include('Category.urls')),
    path('user/', include('profiles.urls')),
    path('message/', include('opt_message.urls')),
    path('company', include('company.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
