from django.db import models

class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True, db_column='stock_id')
    item_name = models.CharField(max_length=100, db_column='item_name')
    quantity = models.IntegerField(db_column='quantity')
    supplier_name = models.CharField(max_length=100, db_column='supplier_name')
    supplier_contact = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'inventory_stock'  # Match db

    def __str__(self):
        return self.item_name

class MenuIngredients(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    menu_item = models.ForeignKey(
        'orders.Menu',
        on_delete=models.CASCADE,
        db_column='menu_item_ID_id'
    )
    stock_item = models.ForeignKey(
        'Stock',
        on_delete=models.CASCADE,
        db_column='stock_ID_id'
    )

    class Meta:
        db_table = 'Inventory_menu_ingredients'  
        unique_together = ('menu_item', 'stock_item')
        verbose_name = 'Menu Ingredient'
        verbose_name_plural = 'Menu Ingredients'

    def __str__(self):
        return f"{self.menu_item.name} requires {self.stock_item.item_name}"