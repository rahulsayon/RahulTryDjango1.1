
from django.contrib import admin
from django.urls import path
from products.views import (product_detail_view,product_create_view,render_initial_data,dynamic_lookup_view,
product_delete_viiew , product_list_view , product_update_view )



urlpatterns = [

path('<int:id>/' , dynamic_lookup_view  , name="products-detail"),
path('<int:id>/delete/' , product_delete_viiew  , name="delete"),
path('' , product_list_view  , name="product-list"),
path('<int:id>/update/' , product_update_view  , name="product-update")


]