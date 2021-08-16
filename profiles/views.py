from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from days.models import Day
from trips.models import Trip
import datetime
import json, requests
#authentication imports
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    '''
    Displays home view. User's current day and the trip they are on alongside the current weather
    '''
    #Declaring variables:
    current_day = None
    current_trip = None
    weather = {}


    
    #Switching between different measurements
    if(request.method == "POST"):
        if(request.POST.get('switch') == "True"):
            units = "metric"
            units_bool = False
            opp_units = "Imperial"

        else:
            units = "imperial"
            units_bool = True
            opp_units = "Metric"
    
    else:
        units = "imperial"
        units_bool = True
        opp_units = "Metric"

    #Getting user
    user_profile = Profile.objects.get(user=request.user)

    #Getting day
    today = datetime.date.today()

    #Checking if there is a planned day today
    try:
        current_day = Day.objects.get(date=today)
        current_trip = Trip.objects.get(pk=current_day.trip.pk, user=user_profile.pk)
    except Day.DoesNotExist:
        current_day = None
    
    if(current_day != None):
        zip_code = current_day.ski_area.zip_code
        
        if(str(current_trip.destination) == "British Columbia"):
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={zip_code},ca&units={units}&appid=b6ac4a5dac5a00f0599a26136811c600")
            weather = response.json()
        
        else:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&units={units}&appid=b6ac4a5dac5a00f0599a26136811c600")
            weather = response.json()

        #Change visibility to miles if units=imperial
        if(units_bool == True):
            weather['visibility'] = weather['visibility'] * 0.000621371192

    context = {
        'current_day':current_day,
        'current_trip':current_trip,
        'weather':weather,
        'units_bool':units_bool,
        'opp_units':opp_units,
    }
    return render(request, "profiles/home.html", context)


@login_required
def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if(form.is_valid()):
        form.save()
        confirm = True
    
    context = {
        'profile':profile,
        'form':form,
        'confirm':confirm,
    }

    return render(request, 'profiles/profile.html', context)