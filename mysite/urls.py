"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
import catalogue.views
import cart.views

urlpatterns = [
  path('', catalogue.views.product_list, name='product_list'),
  path('products/<int:product_id>', catalogue.views.product_detail, name='product_detail'),
  path('products/<int:product_id>/edit/', catalogue.views.product_edit, name='product_edit'),
  path('products/<int:product_id>/delete/', catalogue.views.product_delete, name='product_delete'),
  path('cart/<int:product_id>/add', cart.views.cart_add, name='cart_add'),
  path('cart/', cart.views.cart_list, name='cart_list'),
  path('cart/<int:product_id>/delete/', cart.views.cart_delete, name='cart_delete'),
]
