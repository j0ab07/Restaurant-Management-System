from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages

def list_inventory(request):
    stocks = Stock.objects.all()
    return render(request, 'inventory/list_inventory.html', {'stocks': stocks})

def order_stock(request):
    if request.method == 'POST':
        stock_id = request.POST.get('stock_id')
        quantity = int(request.POST.get('quantity'))

        try:
            stock = Stock.objects.get(id=stock_id)
            stock.quantity += quantity
            stock.save()
            messages.success(request, f"Ordered {quantity} units of {stock.item_name}!")
            return redirect('inventory')
        except Stock.DoesNotExist:
            messages.error(request, "Invalid stock item selected.")

    stocks = Stock.objects.all()
    return render(request, 'inventory/order_stock.html', {'stocks': stocks})