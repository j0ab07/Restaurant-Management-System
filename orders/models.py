from django.db import models
from inventory.models import InventoryItem

class Order(models.Model):
    STATUS_CHOICES = [
        ('Received', 'Received'),
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
        ('Served', 'Served'),
    ]
    order_id = models.AutoField(primary_key=True)
    table_number = models.IntegerField()
    items_ordered = models.ManyToManyField(InventoryItem, related_name='orders')
    quantity = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Received')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - Table {self.table_number}"