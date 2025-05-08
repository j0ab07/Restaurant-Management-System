from django.db import models
from django.contrib.auth import get_user_model

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    allergens = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'orders_menu'  
    
    def __str__(self):
        return f"{self.name} - ${self.price}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    order_id = models.AutoField(primary_key=True)  # Changed from 'id' to 'order_id'
    special_requests = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    time_placed = models.DateTimeField(auto_now_add=True)
    staff_ID = models.ForeignKey(
        'staff_scheduling.Staff',
        on_delete=models.SET_NULL,
        null=True,
        db_column='staff_ID_id'  
    )
    table_ID = models.ForeignKey(
        'reservations.Table',  
        on_delete=models.SET_NULL,
        null=True,
        db_column='table_ID_id'  
    )
    
    class Meta:
        db_table = 'orders_order'  
        
    def __str__(self):
        return f"Order #{self.order_id} - {self.get_status_display()}"  # Updated to use order_id

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    menu_id = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        db_column='menu_id'  
    )
    order_id = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        db_column='order_id' 
    )
    
    class Meta:
        db_table = 'orders_order_items'  
        
class MenuIngredients(models.Model):
    menu_item = models.ForeignKey(
        'Menu',
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    stock_item = models.ForeignKey(
        'inventory.Stock',
        on_delete=models.CASCADE,
        related_name='used_in_menu_items'
    )
    quantity_required = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('menu_item', 'stock_item')

    def __str__(self):
        return f"{self.menu_item.name} requires {self.quantity_required} {self.stock_item.item_name}"
