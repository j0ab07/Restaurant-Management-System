from django.shortcuts import render, redirect
from .models import Reservation, Table
from django.contrib import messages
from datetime import datetime, time

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def submit_reservation(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        table_id = request.POST.get('table_id')
        date = request.POST.get('date')
        time_str = request.POST.get('time')
        number_of_guests = int(request.POST.get('number_of_guests'))

        # Check table availability
        try:
            table = Table.objects.get(table_id=table_id)
            if not table.available or table.max_capacity < number_of_guests:
                messages.error(request, "Table is not available or capacity exceeded.")
                return render(request, 'reservations/submit_reservation.html', {'tables': Table.objects.filter(available=True)})
            
            # Check for conflicting reservations
            existing = Reservation.objects.filter(table_ID=table, date=date, time=time_str, status__in=['Pending', 'Confirmed'])
            if existing.exists():
                messages.error(request, "Table is fully booked for this time.")
                return render(request, 'reservations/submit_reservation.html', {'tables': Table.objects.filter(available=True)})
            
            # Create reservation
            reservation = Reservation.objects.create(
                customer_name=customer_name,
                customer_email=customer_email,
                table_ID=table,
                date=date,
                time=time_str,
                number_of_guests=number_of_guests,
                status='Confirmed'
            )
            table.available = False
            table.save()
            messages.success(request, "Reservation confirmed!")
            return redirect('reservation_list')
        except Table.DoesNotExist:
            messages.error(request, "Invalid table selected.")
    
    return render(request, 'reservations/submit_reservation.html', {'tables': Table.objects.filter(available=True)})