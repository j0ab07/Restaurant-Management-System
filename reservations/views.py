from django.shortcuts import render, redirect
from .models import Reservation
from django.contrib import messages
from datetime import datetime

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def submit_reservation(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        table_number = int(request.POST.get('table_number'))
        date_time = request.POST.get('date_time')
        number_of_guests = int(request.POST.get('number_of_guests'))

        # Check availability 
        existing = Reservation.objects.filter(table_number=table_number, date_time=date_time)
        if existing.exists():
            messages.error(request, "Table is fully booked for this time.")
            return render(request, 'reservations/submit_reservation.html', {'status': 'Fully Booked'})
        
        # Assign table
        reservation = Reservation.objects.create(
            customer_name=customer_name,
            table_number=table_number,
            date_time=date_time,
            number_of_guests=number_of_guests,
            status='Confirmed'
        )
        messages.success(request, "Reservation confirmed!")
        return redirect('reservation_list')
    
    return render(request, 'reservations/submit_reservation.html')