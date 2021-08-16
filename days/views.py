from django.shortcuts import render, redirect
from .models import Day
from trips.models import Trip, Resort
from .forms import DayCreationForm, DayEditForm
import datetime

#AUTH imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def add_day_view(request, **kwargs):
    '''
    Adds a day to a trip
    '''
    #Declaring variables for context
    new_day = None
    day_form = None
    full = 0

    #Getting trip pk and object
    trip_pk = kwargs.get('pk')
    trip = Trip.objects.get(pk=trip_pk)

    #Get destination id
    dest_pk = trip.destination_id

    #Declaring variables to filter availible dates
    date = trip.date_arrived
    dates = []

    #Sense if user submitted new day
    if(request.method == 'POST'):
        #Get variables from form
        day = request.POST.get('date')
        resort = Resort.objects.get(pk=request.POST.get('resort'))
        restaurant = request.POST.get('restaurant')
        
        #Creating new day:
        new_day = Day.objects.create(date=day, ski_area=resort, restaurant=restaurant, trip=trip, user=trip.user)
        full = 3



    #cycle thru dates to find availible dates
    while(date <= trip.date_departed):
        try:
            Day.objects.get(date=date)
        except Day.DoesNotExist:
            dates.append(date)
        date = date + datetime.timedelta(days=1)
    
    #Create a DayCreationForm if there are availible days. If all days have been created and user just created the last one, set full = 4. Else, full = 1
    if(len(dates) != 0):
        day_form = DayCreationForm(dest_pk=dest_pk, dates=dates)
    
    elif(len(dates) == 0 and full == 3):
        full = 4

    else:
        full = 1
    

    
    context = {
        "day_form":day_form,
        "new_day":new_day,
        "full":full,
        "trip_pk":trip_pk,
        "trip_name":trip.trip_name,
    }

    return render(request, 'days/add-day.html', context)


@login_required
def edit_day_view(request, **kwargs):
    '''
    Allows user to edit day
    '''
    #Declaring variables for context:
    day_edit_form = None
    msg = 0
    swapped_day_id = None

    #Getting day and trip
    day_pk = kwargs.get('pk')
    day = Day.objects.get(pk=day_pk)
    trip = day.trip

    #Destination id
    dest_pk = trip.destination_id

    if(request.method == "POST" and "day-delete-btn" in request.POST):
        Trip.objects.get(pk=dest_pk).delete()
        return redirect('/trips')

    elif(request.method == "POST"):
        #Get user input from forms
        user_date = datetime.datetime.strptime(request.POST.get('date'), "%Y-%M-%d").date()
        resort = Resort.objects.get(pk=request.POST.get('resort'))
        restaurant = request.POST.get('restaurant')

        #set alert
        msg = 1

        if(user_date != day.date and Day.objects.filter(date=user_date).exists()):
            msg = 2
            #get swapped day
            swapped_day = Day.objects.get(date=user_date)

            #change its values to previous day and save
            swapped_day.date = day.date
            swapped_day.save()

            #get sapped day id
            swapped_day_id = swapped_day.id

        #Edit day
        day.date = user_date
        day.ski_area = resort
        day.restaurant = restaurant
        day.save()


    #Getting all dates
    start_date = trip.date_arrived
    end_date = trip.date_departed
    dates = []

    #Creating list of dates
    for i in range((end_date-start_date).days + 1):
        if(str(end_date - datetime.timedelta(days=i)) == str(day.date)):
            dates.insert(0, end_date - datetime.timedelta(days=i))
        else:
            dates.append(end_date - datetime.timedelta(days=i))

    #Create form
    day_edit_form = DayEditForm(initial={'day':day.date, 'resort':day.ski_area.pk, 'restaurant':day.restaurant}, dest_pk=dest_pk, dates=dates)

    context = {
        'day_edit_form':day_edit_form,
        'day':day,
        'trip_name':trip.trip_name,
        'trip_pk':trip.pk,
        'msg':msg,
        'swapped_day_id':swapped_day_id,
    }
    # print(day.date, type(day.date))
    return render(request, 'days/edit-day.html', context)


