from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderItem, Menu
from .forms import AddMenuItemForm, MenuIngredientForm
from reservations.models import Table
from staff_scheduling.models import Staff

# View to display all menu items
def menu(request):
    menu_items = Menu.objects.all().order_by('name')
    print(f"DEBUG MENU ITEMS: {list(menu_items)}")
    return render(request, 'orders/menu.html', {
        'menu_items': menu_items,
        'debug': True,
    })

# View to list all orders
def list_orders(request):
    orders = Order.objects.all().select_related('staff_ID', 'table_ID')
    return render(request, 'orders/list_orders.html', {'orders': orders})

# View to place a new order
def place_order(request):
    if request.method == 'POST':
        try:
            table_no = request.POST.get('table_no')
            staff_id = request.POST.get('staff_id')
            table = Table.objects.filter(table_no=table_no, available=True).first()
            if not table:
                raise ValueError(f"Table {table_no} doesn't exist or is unavailable")
            if not Staff.objects.filter(id=staff_id).exists():
                raise ValueError(f"Staff {staff_id} doesn't exist")

            order = Order.objects.create(
                special_requests=request.POST.get('special_requests', ''),
                status='pending',
                staff_ID_id=staff_id,
                table_ID=table
            )

            menu_item_ids = request.POST.getlist('menu_items')
            for item_id in menu_item_ids:
                OrderItem.objects.create(
                    menu_id_id=item_id,
                    order_id=order
                )

            messages.success(request, f"Order #{order.order_id} created successfully!")
            return redirect('list_orders')

        except Exception as e:
            messages.error(request, f"Error placing order: {str(e)}")
            return redirect('place_order')

    menus = Menu.objects.all()
    staff_members = Staff.objects.all()
    tables = Table.objects.filter(available=True).order_by('table_no')
    return render(request, 'orders/place_order.html', {
        'menus': menus,
        'staff': staff_members,
        'tables': tables,
    })

# View to update order status
def prepare_order(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        order.status = status
        order.save()
        messages.success(request, "Order status updated!")
        return redirect('list_orders')
    return render(request, 'orders/prepare_order.html', {'order': order})

# View to add a new menu item
def add_menu_item(request):
    if request.method == 'POST':
        form = AddMenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu item added successfully!")
            return redirect('menu')
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = AddMenuItemForm()
    return render(request, 'orders/add_menu_item.html', {'form': form})

# View to display menu item details and manage ingredients
def menu_item_detail(request, item_id):
    menu_item = get_object_or_404(Menu, menu_id=item_id)
    ingredients = menu_item.ingredients.all()
    if request.method == 'POST':
        form = MenuIngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.menu_item = menu_item
            ingredient.save()
            return redirect('menu_item_detail', item_id=item_id)
    else:
        form = MenuIngredientForm()
    return render(request, 'orders/menu_item_detail.html', {
        'menu_item': menu_item,
        'ingredients': ingredients,
        'form': form,
    })

# View to confirm order details
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    return render(request, 'orders/order_confirmation.html', {'order': order})