from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Staff, Schedule, TimeOffRequest
from django.contrib import messages

def list_staff(request):
    staff = Staff.objects.all()
    return render(request, 'staff_scheduling/list_staff.html', {'staff': staff})

def all_schedules(request):
    staff_members = Staff.objects.all()
    schedules = Schedule.objects.all().order_by('shift_date', 'start_time')
    return render(request, 'staff_scheduling/all_schedules.html', {
        'staff_members': staff_members,
        'schedules': schedules
    })

def request_time_off(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        additional_info = request.POST.get('reason')  

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
            return redirect('list_staff')
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
        return redirect('list_staff')
    return render(request, 'staff_scheduling/manage_time_off.html', {'request': time_off_request})

def create_schedule(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        shift_date = request.POST.get('shift_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        try:
            staff = Staff.objects.get(id=staff_id)
            Schedule.objects.create(
                staff_id=staff,
                shift_date=shift_date,
                start_time=start_time,
                end_time=end_time
            )
            messages.success(request, "Schedule created successfully!")
            return redirect('list_staff')
        except Staff.DoesNotExist:
            messages.error(request, "Invalid staff selected.")

    staff = Staff.objects.all()
    return render(request, 'staff_scheduling/create_schedule.html', {'staff': staff})

def create_staff(request):
    if request.method == 'POST':
        name = request.POST.get('staff_name')
        role = request.POST.get('staff_role')
        email = request.POST.get('staff_email')

        if name and role and email:
            Staff.objects.create(
                staff_name=name,
                staff_role=role,
                staff_email=email
            )
            messages.success(request, "Staff member created successfully!")
            return redirect('list_staff')
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'staff_scheduling/create_staff.html')