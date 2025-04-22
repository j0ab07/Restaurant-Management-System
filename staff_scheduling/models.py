from django.db import models

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=100)
    staff_role = models.CharField(max_length=50)
    staff_email = models.CharField(max_length=50)
    time_off_allowance = models.FloatField(default=0)

    def __str__(self):
        return self.staff_name

class Schedule(models.Model):
    staff_id = models.ForeignKey(Staff, primary_key= True, on_delete=models.CASCADE, related_name='Schedule')
    date = models.DateField
    shift_start = models.TimeField
    shift_end = models.TimeField

    def __str__(self):
        return f"Staff: {self.staff_id.staff_name} Shift: {self.date}, {self.shift_start} - {self.shift_end}"

class TimeOffRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Denied', 'Denied'),
    ]
    request_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='time_off_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    additional_info = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Staff: {self.staff_id.staff_name} Request: {self.request_id}"