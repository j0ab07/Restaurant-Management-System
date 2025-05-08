from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_inventory, name='inventory'),
    path('order/', views.order_stock, name='order_stock'),
    path('add/', views.add_stock, name='add_stock'),
]