from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock
from .forms import AddStockForm

# View to list all inventory items
def list_inventory(request):
    stocks = Stock.objects.all()
    low_stock = Stock.objects.filter(quantity__lt=10)
    return render(request, 'inventory/list_inventory.html', {
        'stocks': stocks,
        'low_stock': low_stock
    })

# View to handle stock ordering
def order_stock(request):
    if request.method == 'POST':
        stock_id = request.POST.get('stock_id')
        quantity = request.POST.get('quantity', 0)
        
        try:
            stock = Stock.objects.get(stock_id=stock_id)
            stock.quantity += int(quantity)
            stock.save()
            messages.success(request, f"Added {quantity} units of {stock.item_name}")
            return redirect('inventory')
        except (Stock.DoesNotExist, ValueError) as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('order_stock')
    
    stocks = Stock.objects.all()
    return render(request, 'inventory/order_stock.html', {'stocks': stocks})

# View to add new stock items
def add_stock(request):
    if request.method == 'POST':
        form = AddStockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = AddStockForm()
    return render(request, 'inventory/add_stock.html', {'form': form})