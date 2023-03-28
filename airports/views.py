from django.http import HttpResponse
from django.shortcuts import render  # important to render library to make loading templates easier.
from .models import Airport


def index(request):
    # Fetch all airports from database
    airports = Airport.objects.all()
    context = {'airports': airports}
    return render(request, 'airports/index.html', context)

def search(request):
    form = TicketForm(request.POST)
    if form.is_valid():
        reservation = Reservation.objects.get(id=form.cleaned_data['confirmation_number'])
        return render(request, 'tickets/ticket_search.html', {'reservation': reservation})

def search1(request):
    form = FlightForm(request.POST)
    if form.is_valid():
        origin = Origin.objects.get(id=form.cleaned_data['origin'])
        destination = Destination.objects.get(id=form.cleaned_data['destination'])
        return render(request, 'flights/flight_search.html', {'origin': origin}, {'destination': destination})


def airport_info(request, airport_code):
    # Fetch the airport by a certain code
    # Remember as we are only expecting one airport per code we should use get
    airport = Airport.objects.get(airport_code=airport_code)
    context = {'airport': airport}
    # Display the airport name and code
    return render(request, 'airports/index.html', context)
    # Display the airport name and code
