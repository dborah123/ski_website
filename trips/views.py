from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import TripCreationForm
from .models import Trip, Destination
from profiles.models import Profile
from days.models import Day
from datetime import date
import json

#AUTH imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def home_view(request):
    '''
    FOR 'home.html'

    Creates a trip form and submits it if user desires
    '''
    trip_form = TripCreationForm(request.POST or None)
    new_trip = None
    trip_created = 0

    if(request.method == 'POST'):
        # Retrieving items from form
        trip_name = request.POST.get('trip_name')
        date_arrived = request.POST.get('date_arrived')
        date_departed = request.POST.get('date_departed')
        hotel = request.POST.get('hotel')
        user = Profile.objects.get(pk=int(request.POST.get('user')))
        destination = Destination.objects.get(pk=int(request.POST.get('destination')))

        if(Trip.objects.filter(
            Q(user=user, date_arrived__range=[date_arrived, date_departed]) |
            Q(user=user, date_departed__range=[date_arrived, date_departed]) | 
            Q(user=user, date_departed__lte=date_departed, date_arrived__gte=date_arrived)
        )):
            trip_created = 2
        else:
            new_trip = Trip.objects.get_or_create(trip_name=trip_name, date_arrived=date_arrived, date_departed=date_departed, hotel=hotel, user=user, destination=destination)
            trip_created = 1
        


    context = {
        'trip_form':trip_form,
        'new_trip':new_trip,
        'trip_created':trip_created,
    }

    return render(request, 'trips/home.html', context)
    

@login_required
def trips_view(request):
    '''
    FOR 'trips.html'

    Displays the various trips the signed in user has created
    '''

    if(request.method == "POST"):
        Trip.objects.get(pk=request.POST['pk']).delete()


    #Querying data for user's trips:

    user_qset = Profile.objects.filter(user=request.user)

    future_trips_list = []
    past_trips_list = []
    current_trips_list = []
    for trip in Trip.objects.filter(user=user_qset[0]):
        d = {
            "trip_name":trip.trip_name,
            "destination":str(trip.destination),
            "date_arrived":str(trip.date_arrived),
            "date_departed":str(trip.date_departed),
            "hotel":trip.hotel,
            "id":trip.id,
        }

        if(date.today() > trip.date_departed):
            d['number'] = len(past_trips_list)
            past_trips_list.append(d)

        elif(date.today() < trip.date_arrived):
            d['number'] = len(future_trips_list)
            future_trips_list.append(d)

        else:
            d['number'] = len(current_trips_list)
            current_trips_list.append(d)


    context = {
        'past_trips':past_trips_list,
        'current_trips':current_trips_list,
        'planned_trips':future_trips_list,
    }


    return render(request, 'trips/trips.html', context)


@login_required
def trip_details_view(request, **kwargs):
    '''
    Returns the details of a singular trip
    '''
    pk = kwargs.get('pk')

    if(request.method == "POST"):
        #Deletes trip object and reroutes user to trip overview
        Trip.objects.get(pk=pk).delete()
        return redirect('/trips')

    else:
        trip = Trip.objects.get(pk=pk)
        days = Day.objects.filter(trip=pk).order_by('date')

        return render(request, 'trips/detail.html', {'trip':trip, 'days':days})