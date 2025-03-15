from django.db import models

class InventoryItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    quantity_on_hand = models.IntegerField()
    reorder_level = models.IntegerField()
    supplier_info = models.TextField()

    def __str__(self):
        return self.item_name