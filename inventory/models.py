from django.db import models
from orders.models import Menu

class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    supplier_name = models.CharField(max_length=100)
    supplier_contact = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name
    
    class Menu_Ingredients(models.Model):
        menu_item_ID = models.ForeignKey(Menu, primary_key=True)
        stock_ID = models.ForeignKey(Stock, primary_key=True)