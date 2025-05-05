from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem, Menu
from reservations.models import Table  
from staff_scheduling.models import Staff  
from django.contrib import messages

def list_orders(request):
    orders = Order.objects.all().select_related('staff_ID', 'table_ID')
    return render(request, 'orders/list_orders.html', {'orders': orders})

def place_order(request):
    if request.method == 'POST':
        try:
            # Create the order
            order = Order.objects.create(
                special_requests=request.POST.get('special_requests', ''),
                status='pending',
                staff_id=request.POST.get('staff_id'),
                table_id=request.POST.get('table_no')
            )
            
            # Add menu items to order
            menu_item_ids = request.POST.getlist('menu_items')
            for item_id in menu_item_ids:
                OrderItem.objects.create(
                    menu_id_id=item_id,  
                    order_id=order
                )
            
            messages.success(request, "Order placed successfully!")
            return redirect('order_confirmation', order_id=order.order_id)
            
        except Exception as e:
            messages.error(request, f"Error placing order: {str(e)}")
            return redirect('place_order')
    
    menus = Menu.objects.all()
    staff_members = Staff.objects.all()
    tables = range(1, 21)  
    
    return render(request, 'orders/place_order.html', {
        'menus': menus,
        'staff': staff_members,
        'tables': tables
    })

def prepare_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        order.status = status
        order.save()
        messages.success(request, "Order status updated!")
        return redirect('orders')
    return render(request, 'orders/prepare_order.html', {'order': order})