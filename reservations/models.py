from django.db import models

class Table(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_no = models.IntegerField()
    max_capacity = models.IntegerField()
    available = models.BooleanField()

    def __str__(self):
        return f"{self.table_no}"

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Fully Booked', 'Fully Booked'),
    ]
    reservation_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    table_ID = models.ForeignKey(Table,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.customer_name} - {self.date}, {self.time}"
    
