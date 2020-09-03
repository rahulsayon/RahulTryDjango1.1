"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
# from pages.views import home_view,social_view,contract_view,about_view
from products.views import (product_detail_view,product_create_view,render_initial_data,dynamic_lookup_view,
product_delete_viiew , product_list_view , product_update_view )

from profiles.views import get_data


urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/' , product_detail_view  , name="details"),
    path('create/' , product_create_view  , name="create"),
    path('product/' , include(('products.urls','products' ), namespace='products')  ),
    path('article/' , include(('blog.urls','blog' ), namespace='blog')  ),
    path('course/' , include(('courses.urls','courses' ), namespace='course')  ),
    path("get_data/" , get_data )

    # # path('product/<int:id>' , render_initial_data  , name="render")
    



]
