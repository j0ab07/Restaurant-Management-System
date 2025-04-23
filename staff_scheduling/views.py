from django.shortcuts import render, redirect
from .models import Staff, TimeOffRequest
from .strategy import ApproveStrategy, DenyStrategy
from django.contrib import messages

def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'staff_scheduling/staff_list.html', {'staff_members': staff_members})

def request_time_off(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        additional_info = request.POST.get('additional_info', '')
        try:
            staff = Staff.objects.get(staff_id=staff_id)
            TimeOffRequest.objects.create(
                staff_id=staff,
                start_date=start_date,
                end_date=end_date,
                additional_info=additional_info,
                status='Pending'
            )
            messages.success(request, "Time-off request submitted!")
            return redirect('staff_list')
        except Staff.DoesNotExist:
            messages.error(request, "Invalid staff selected.")
    return render(request, 'staff_scheduling/request_time_off.html', {'staff_members': Staff.objects.all()})

def manage_time_off(request, request_id):
    time_off_request = TimeOffRequest.objects.get(request_id=request_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        strategy = ApproveStrategy() if status == 'Approved' else DenyStrategy()
        strategy.process_request(time_off_request)
        messages.success(request, f"Time-off request {status.lower()}!")
        return redirect('staff_list')
    return render(request, 'staff_scheduling/manage_time_off.html', {'time_off_request': time_off_request})