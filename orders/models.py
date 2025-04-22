from django.db import models
from reservations.models import Table
from staff_scheduling.models import Staff

class Order(models.Model):
    STATUS_CHOICES = [
        ('Received', 'Received'),
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
        ('Served', 'Served'),
    ]
    order_id = models.AutoField(primary_key=True)
    table_ID = models.ForeignKey(Table, on_delete=models.CASCADE)
    staff_ID = models.ForeignKey(Staff, on_delete=models.CASCADE)
    special_requests = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Received')
    time_placed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - Table {self.table_ID}"
    
class Menu(models.Model):
    menu_item_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    allergens = models.TextField(blank = True, null = True)

    def __str__(self):
        return f"{self.name}"

class Order_Items(models.Model):
    order_ID = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_ID = models.ForeignKey(Menu, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('order_ID', 'item_ID')

