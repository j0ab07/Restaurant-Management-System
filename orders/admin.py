# orders/admin.py
from django.contrib import admin
from .models import Menu, Order, Order_Items

admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Order_Items)

