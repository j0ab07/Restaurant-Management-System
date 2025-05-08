from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem, Menu
from .forms import AddMenuItemForm, MenuIngredientForm
from reservations.models import Table  
from staff_scheduling.models import Staff  
from django.contrib import messages

def menu(request):
    menu_items = Menu.objects.all().order_by('name')
    print(f"DEBUG MENU ITEMS: {list(menu_items)}")  # Check console output
    return render(request, 'orders/menu.html', {
        'menu_items': menu_items,
        'debug': True  # Add debug flag to template
    })

def list_orders(request):
    orders = Order.objects.all().select_related('staff_ID', 'table_ID')
    return render(request, 'orders/list_orders.html', {'orders': orders})

def place_order(request):
    if request.method == 'POST':
        try:
            # Get the table number from form (not table_id)
            table_no = request.POST.get('table_no')
            staff_id = request.POST.get('staff_id')
            
            # Find table by table_no (not id)
            table = Table.objects.filter(table_no=table_no, available=True).first()
            if not table:
                raise ValueError(f"Table {table_no} doesn't exist or is unavailable")
                
            if not Staff.objects.filter(id=staff_id).exists():
                raise ValueError(f"Staff {staff_id} doesn't exist")
            
            # Create the order with the table object
            order = Order.objects.create(
                special_requests=request.POST.get('special_requests', ''),
                status='pending',
                staff_ID_id=staff_id,
                table_ID=table  # Use the table object directly
            )
            
            # Add menu items to order
            menu_item_ids = request.POST.getlist('menu_items')
            for item_id in menu_item_ids:
                OrderItem.objects.create(
                    menu_id_id=item_id,
                    order_id=order
                )
            
            messages.success(request, "Order placed successfully!")
            messages.success(request, f"Order #{order.order_id} created successfully!")  # Use order_id

            return redirect('list_orders')
            
        except Exception as e:
            messages.error(request, f"Error placing order: {str(e)}")
            return redirect('place_order')
    
    # GET request handling
    menus = Menu.objects.all()
    staff_members = Staff.objects.all()
    tables = Table.objects.filter(available=True).order_by('table_no')
    
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

def add_menu_item(request):
    if request.method == 'POST':
        form = AddMenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu item added successfully!")
            return redirect('menu')  # Redirect to menu page after adding
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = AddMenuItemForm()
    return render(request, 'orders/add_menu_item.html', {'form': form})

def menu_item_detail(request, item_id):
    menu_item = get_object_or_404(Menu, id=item_id)
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
        'form': form
    })
    
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_confirmation.html', {'order': order})