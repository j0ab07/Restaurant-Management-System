from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('submit/', views.submit_reservation, name='submit_reservation'),
]