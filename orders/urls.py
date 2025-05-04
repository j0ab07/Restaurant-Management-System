from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_orders, name='orders'),
    path('place/', views.place_order, name='place_order'),
    path('prepare/<int:order_id>/', views.prepare_order, name='prepare_order'),
]