from django.db import models

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Fully Booked', 'Fully Booked'),
    ]
    reservation_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    table_number = models.IntegerField()
    date_time = models.DateTimeField()
    number_of_guests = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.customer_name} - {self.date_time}"