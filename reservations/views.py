from django.shortcuts import render
from .models import Reservation

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})