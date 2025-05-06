# staff_scheduling/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Staff(models.Model):
    staff_name = models.CharField(max_length=100)
    staff_role = models.CharField(max_length=50)
    staff_email = models.EmailField(unique=True)

    def __str__(self):
        return self.staff_name

class Schedule(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE) 
    shift_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Schedule for {self.staff_id} on {self.shift_date}"

class TimeOffRequest(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    additional_info = models.TextField() 
    status = models.CharField(max_length=20, default='Pending') 
    
    def __str__(self):
        return f"Time off request by {self.staff}"