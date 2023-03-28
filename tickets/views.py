from django.http import HttpResponse
from django.shortcuts import render
from .models import Reservation
from .forms import TicketForm

def index(request):
    form = TicketForm()
    return render(request, 'tickets/index.html', {'form': form})

def ticket_search(request, confirmation_number):
    # Select the singular reservation for the confirmation number
    # Note: the confirmation_number is the id in the Reservation table
    reservation = Reservation.objects.get(pk=confirmation_number)
    return HttpResponse('Number of tickets for confirmation number: ' + str(confirmation_number) + " is " + str(reservation.num_people))
