from django.db import models
from flights.models import Flight
# Create your models here.
class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    num_people = models.IntegerField()
    total_cost = models.DecimalField(max_digits=5, decimal_places=2)
class Ticket(models.Model):
    # Ticket Classes
    First_Class = 'F'
    Business_Class = 'B'
    Main_Cabin = 'M'
    Ticket_Class_Choices = [
        (First_Class, 'First Class'),
        (Business_Class, 'Business Class'),
        (Main_Cabin, 'Main Cabin'),
    ]
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT)
    seat = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_class = models.CharField(
        max_length=1,
        choices=Ticket_Class_Choices,
    )

