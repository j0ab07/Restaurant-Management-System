from django.contrib import admin
from django.urls import path, include
from . import views

# Main URL patterns for the restaurant_management project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', include('staff_scheduling.urls')),
    path('orders/', include('orders.urls')),
    path('reservations/', include('reservations.urls')),
    path('inventory/', include('inventory.urls')),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('menu/', views.menu, name='menu'),
]