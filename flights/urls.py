# Load path from django.urls
from django.urls import path
# Load this application's views.py file
from . import views

# Define url patterns
urlpatterns = [
    # Get index view
    # Example url: /airports/
    path('/', views.index),
    # Show Airport info
    # Example url /airports/MYR
    # NOTICE: the airport_code parameter in the url matches
    #       the parameter in the airport_info function
    path('/search/<str:origin>/<str:destination>/', views.flight_search),
]