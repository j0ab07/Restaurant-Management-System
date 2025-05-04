# orders/models.py
from django.db import models

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    allergens = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)  # Match the database schema
    table_ID = models.ForeignKey('reservations.Table', on_delete=models.CASCADE)
    staff_ID = models.ForeignKey('staff_scheduling.Staff', on_delete=models.CASCADE)
    special_requests = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='Received')
    time_placed = models.DateTimeField(auto_now_add=True)  # Match the database schema

    def __str__(self):
        return f"Order #{self.order_id} - Table {self.table_ID.table_no}"

class Order_Items(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.menu.name} in Order #{self.order.order_id}"