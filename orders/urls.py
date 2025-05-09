from django.urls import path
from . import views

# URL patterns for orders app
urlpatterns = [
    path('menu/', views.menu, name='menu'),  
    path('orders/menu/add/', views.add_menu_item, name='add_menu_item'),  # Admin-only add form
    path('orders/', views.list_orders, name='list_orders'),
    path('orders/place/', views.place_order, name='place_order'),
    path('orders/prepare/<int:order_id>/', views.prepare_order, name='prepare_order'),
    path('orders/confirm/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('orders/item/<int:item_id>/', views.menu_item_detail, name='menu_item_detail'),
]