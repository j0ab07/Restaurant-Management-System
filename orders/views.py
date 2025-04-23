from django.shortcuts import render, redirect
from .models import Order, Menu, Order_Items
from reservations.models import Table
from staff_scheduling.models import Staff
from django.contrib import messages

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def place_order(request):
    if request.method == 'POST':
        table_id = request.POST.get('table_id')
        staff_id = request.POST.get('staff_id')
        item_ids = request.POST.getlist('item_ids')  # List of menu item IDs
        special_requests = request.POST.get('special_requests', '')

        try:
            table = Table.objects.get(table_id=table_id)
            staff = Staff.objects.get(staff_id=staff_id)
            order = Order.objects.create(
                table_ID=table,
                staff_ID=staff,
                special_requests=special_requests,
                status='Received'
            )
            # Add items to order
            for item_id in item_ids:
                menu_item = Menu.objects.get(menu_item_ID=item_id)
                Order_Items.objects.create(order_ID=order, item_ID=menu_item)
            messages.success(request, "Order placed successfully!")
            return redirect('order_list')
        except (Table.DoesNotExist, Staff.DoesNotExist, Menu.DoesNotExist):
            messages.error(request, "Invalid table, staff, or menu item selected.")

    return render(request, 'orders/place_order.html', {
        'tables': Table.objects.filter(available=False),  # Only reserved tables
        'staff': Staff.objects.all(),
        'menu_items': Menu.objects.all()
    })

def prepare_order(request, order_id):
    order = Order.objects.get(order_id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        if new_status == 'Served':
            # Update stock (if linked via Menu_Ingredients)
            for item in order.order_items_set.all():
                menu_item = item.item_ID
                ingredients = menu_item.menu_ingredients_set.all()
                for ingredient in ingredients:
                    stock = ingredient.stock_ID
                    stock.quantity -= 1  # Simplified; adjust based on recipe
                    stock.save()
        order.save()
        messages.success(request, "Order status updated!")
        return redirect('order_list')
    return render(request, 'orders/prepare_order.html', {'order': order})