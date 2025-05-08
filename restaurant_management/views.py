from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/home/')
    return render(request, 'home.html')

def menu(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/menu/')
    return render(request, 'menu.html')

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