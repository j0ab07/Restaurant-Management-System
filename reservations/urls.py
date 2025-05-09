from django.urls import path
from . import views

# URL patterns for reservations app
urlpatterns = [
    path('', views.reservations, name='reservations'),
]