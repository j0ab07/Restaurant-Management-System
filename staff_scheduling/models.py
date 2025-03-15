from django.db import models

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    shift_times = models.CharField(max_length=100)  # e.g., "9:00-17:00"
    hours_worked = models.FloatField(default=0)

    def __str__(self):
        return self.name