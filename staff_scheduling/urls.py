from django.urls import path
from . import views

# URL patterns for staff_scheduling app
urlpatterns = [
    path('', views.list_staff, name='list_staff'),
    path('time-off/request/', views.request_time_off, name='request_time_off'),
    path('time-off/manage/<int:request_id>/', views.manage_time_off, name='manage_time_off'),
    path('schedules/', views.all_schedules, name='all_schedules'),
    path('schedule/create/', views.create_schedule, name='create_schedule'),
    path('staff/create/', views.create_staff, name='create_staff'),
]