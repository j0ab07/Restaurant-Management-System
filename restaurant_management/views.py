from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/home/')
    return render(request, 'home.html')

def menu(request):
    from orders.models import Menu  # Import the Menu model
    menu_items = Menu.objects.all().order_by('name')
    return render(request, 'orders/menu.html', {
        'menu_items': menu_items
    })

def contact(request):
    if request.method == 'POST':
        # Handle contact form submission (e.g., send email or save to database)
        # For now, just redirect
        return HttpResponseRedirect('/contact/')
    return render(request, 'contact.html')

def login(request):
    if request.method == 'POST':
        # Handle login logic (e.g., authenticate user)
        # For now, just redirect
        return HttpResponseRedirect('/login/')
    return render(request, 'login.html')