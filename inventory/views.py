from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages

def inventory_list(request):
    stock_items = Stock.objects.all()
    low_stock = [item for item in stock_items if item.quantity <= 10]  # Arbitrary threshold
    return render(request, 'inventory/inventory_list.html', {'stock_items': stock_items, 'low_stock': low_stock})

def order_stock(request):
    if request.method == 'POST':
        stock_id = request.POST.get('stock_id')
        quantity = int(request.POST.get('quantity'))
        try:
            stock = Stock.objects.get(stock_id=stock_id)
            stock.quantity += quantity
            stock.save()
            messages.success(request, f"Ordered {quantity} units of {stock.item_name}.")
            return redirect('inventory_list')
        except Stock.DoesNotExist:
            messages.error(request, "Invalid stock item selected.")
    return render(request, 'inventory/order_stock.html', {'stock_items': Stock.objects.all()})