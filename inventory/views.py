from django.shortcuts import render, redirect
from .models import InventoryItem, Supplier
from django.contrib import messages

def inventory_list(request):
    inventory_items = InventoryItem.objects.all()
    low_stock = [item for item in inventory_items if item.quantity_on_hand <= item.reorder_level]
    return render(request, 'inventory/inventory_list.html', {'inventory_items': inventory_items, 'low_stock': low_stock})

def order_stock(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))
        item = InventoryItem.objects.get(item_id=item_id)
           # Simulation (need database to be implemented for data)
        item.quantity_on_hand += quantity
        item.save()
        messages.success(request, f"Ordered {quantity} units of {item.item_name}.")
        return redirect('inventory_list')
    return render(request, 'inventory/order_stock.html', {'items': InventoryItem.objects.all()})