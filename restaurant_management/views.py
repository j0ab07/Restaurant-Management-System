from django.shortcuts import render
from django.http import HttpResponseRedirect
from orders.models import Menu

# View for the homepage
def home(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/home/')
    return render(request, 'home.html')

# View to display the restaurant menu
def menu(request):
    menu_items = Menu.objects.all().order_by('name')
    return render(request, 'orders/menu.html', {'menu_items': menu_items})

# View for the contact page
def contact(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/contact/')
    return render(request, 'contact.html')

# View for the login page
def login(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/login/')
    return render(request, 'login.html')