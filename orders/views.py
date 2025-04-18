from django.shortcuts import render, redirect
from .models import Order
from inventory.models import InventoryItem
from django.contrib import messages

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def place_order(request):
    if request.method == 'POST':
        table_number = int(request.POST.get('table_number'))
        item_ids = request.POST.getlist('items_ordered')  # List of item IDs
        quantity = int(request.POST.get('quantity'))
        special_requests = request.POST.get('special_requests', '')

        # Check stock
        for item_id in item_ids:
            item = InventoryItem.objects.get(id=item_id)
            if item.quantity_on_hand < quantity:
                messages.error(request, f"Item {item.item_name} is out of stock.")
                return render(request, 'orders/place_order.html', {'inventory_items': InventoryItem.objects.all()})

        # Create order
        order = Order.objects.create(
            table_number=table_number,
            quantity=quantity,
            special_requests=special_requests,
            status='Received'
        )
        order.items_ordered.set(item_ids)
        messages.success(request, "Order placed successfully!")
        return redirect('order_list')

    return render(request, 'orders/place_order.html', {'inventory_items': InventoryItem.objects.all()})

def prepare_order(request, order_id):
    order = Order.objects.get(order_id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        if new_status == 'Served':
            # Update stock
            for item in order.items_ordered.all():
                item.quantity_on_hand -= order.quantity
                item.save()
        order.save()
        messages.success(request, "Order status updated!")
        return redirect('order_list')
    return render(request, 'orders/prepare_order.html', {'order': order})