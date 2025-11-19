from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path("products/",views.products,name="products"),
    path('products', views.products_list, name='products'),  # /products/
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # detail page
]