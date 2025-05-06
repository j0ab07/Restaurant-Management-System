from django.shortcuts import render, redirect
from staff_scheduling.models import Staff, Schedule
from .models import Reservation, Table
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, time

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})


def reservations(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        date = request.POST.get('date')
        time_str = request.POST.get('time')
        number_of_guests = int(request.POST.get('number_of_guests'))

        try:
            table = Table.objects.filter(
                available=True,
                max_capacity__gte=number_of_guests
            ).first()

            if not table:
                messages.error(request, "No available tables for the requested number of guests.")
                return render(request, 'reservations/reservations.html')

            # Check for conflicting reservations
            existing = Reservation.objects.filter(
                table_ID=table,
                date=date,
                time=time_str,
                status__in=['Pending', 'Confirmed']
            )
            if existing.exists():
                messages.error(request, "Table is fully booked for this time.")
                return render(request, 'reservations/reservations.html')

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

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'reservations/reservations.html')

    return render(request, 'reservations/reservations.html')


