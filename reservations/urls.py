from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservations, name='reservations'),
    path('list/', views.reservation_list, name='reservation_list'),
]