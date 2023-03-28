from django.http import HttpResponse
from django.shortcuts import render
from .models import Flight  # Import Flight model
from airports.models import Airport  # Import airport model to get airport id and code
from .forms import FlightForm
def index(request):
    # Fetch all flights
    form = FlightForm()
    return render(request, 'flights/index.html', {'form': form})


def flight_search(request, origin, destination):
    origin = Airport.objects.get(airport_code=origin)
    destination = Airport.objects.get(airport_code=destination)
    # Code to select flights from the database
    flight = Flight.objects.field(pk=flight_search)
    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " +
                             f.airline.airline_code for f in flight])
    return HttpResponse('Showing flights: ' + flight_list)
