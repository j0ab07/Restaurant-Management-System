from django.db import models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    table_number = models.IntegerField()
    items_ordered = models.TextField()  # Could be a ManyToManyField to a MenuItem model
    quantity = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Received', 'Received'), ('Preparing', 'Preparing'), ('Ready', 'Ready'), ('Served', 'Served')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - Table {self.table_number}"