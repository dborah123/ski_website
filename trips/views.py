from django.shortcuts import render
from .forms import TripCreationForm
from .models import Trip, Destination
from profiles.models import Profile

# Create your views here.

def home_view(request):
    trip_form = TripCreationForm(request.POST or None)
    new_trip = None
    trip_created = False

    if(request.method == 'POST'):
        # Retrieving items from form
        trip_name = request.POST.get('trip_name')
        date_arrived = request.POST.get('date_arrived')
        date_departed = request.POST.get('date_departed')
        hotel = request.POST.get('hotel')
        user = Profile.objects.get(pk=int(request.POST.get('user')))
        destination = Destination.objects.get(pk=int(request.POST.get('destination')))

        new_trip = Trip.objects.get_or_create(trip_name=trip_name, date_arrived=date_arrived, date_departed=date_departed, hotel=hotel, user=user, destination=destination)

        trip_created=True




    context = {
        'trip_form':trip_form,
        'new_trip':new_trip,
        'trip_created':trip_created,
    }

    return render(request, 'trips/home.html', context)