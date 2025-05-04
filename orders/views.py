from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Order_Items, Menu
from reservations.models import Table  # Import Table from reservations.models
from staff_scheduling.models import Staff  # Import Staff from staff_scheduling.models
from django.contrib import messages

def list_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/list_orders.html', {'orders': orders})

def place_order(request):
    if request.method == 'POST':
        table_id = request.POST.get('table_id')
        staff_id = request.POST.get('staff_id')
        menu_items = request.POST.getlist('menu_items')
        special_requests = request.POST.get('special_requests')

        try:
            table = Table.objects.get(table_id=table_id, available=True)
            staff = Staff.objects.get(id=staff_id)

            # Create the order
            order = Order.objects.create(
                table_ID=table,
                staff_ID=staff,
                special_requests=special_requests,
                status='Received'
            )

            # Add menu items to the order
            for menu_id in menu_items:
                menu = Menu.objects.get(id=menu_id)
                Order_Items.objects.create(order=order, menu=menu)

            messages.success(request, "Order placed successfully!")
            return redirect('orders')

        except (Table.DoesNotExist, Staff.DoesNotExist, Menu.DoesNotExist) as e:
            messages.error(request, f"Error placing order: {str(e)}")

    tables = Table.objects.filter(available=True)
    staff = Staff.objects.all()
    menus = Menu.objects.all()
    return render(request, 'orders/place_order.html', {'tables': tables, 'staff': staff, 'menus': menus})

def prepare_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        order.status = status
        order.save()
        messages.success(request, "Order status updated!")
        return redirect('orders')
    return render(request, 'orders/prepare_order.html', {'order': order})