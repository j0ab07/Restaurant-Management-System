from django.shortcuts import render, redirect, get_object_or_404
from .models import Staff, TimeOffRequest
from django.contrib import messages

def list_staff(request):
    staff = Staff.objects.all()
    return render(request, 'staff_scheduling/list_staff.html', {'staff': staff})

def request_time_off(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        additional_info = request.POST.get('additional_info')

        try:
            staff = Staff.objects.get(id=staff_id)
            TimeOffRequest.objects.create(
                staff=staff,
                start_date=start_date,
                end_date=end_date,
                additional_info=additional_info,
                status='Pending'
            )
            messages.success(request, "Time-off request submitted!")
            return redirect('staff')
        except Staff.DoesNotExist:
            messages.error(request, "Invalid staff selected.")

    staff = Staff.objects.all()
    return render(request, 'staff_scheduling/request_time_off.html', {'staff': staff})

def manage_time_off(request, request_id):
    time_off_request = get_object_or_404(TimeOffRequest, id=request_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        time_off_request.status = status
        time_off_request.save()
        messages.success(request, "Time-off request updated!")
        return redirect('staff')
    return render(request, 'staff_scheduling/manage_time_off.html', {'request': time_off_request})