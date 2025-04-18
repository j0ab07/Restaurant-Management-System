from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('time-off/request/', views.request_time_off, name='request_time_off'),
    path('time-off/manage/<int:request_id>/', views.manage_time_off, name='manage_time_off'),
]