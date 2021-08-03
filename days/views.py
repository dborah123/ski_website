from django.shortcuts import render
from .models import Day
from trips.models import Trip
from .forms import DayCreationForm

#AUTH imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def add_day_view(request, **kwargs):
    '''
    Adds a day to a trip
    '''
    pk = kwargs.get('pk')
    day_form = DayCreationForm(request.POST or None, pk)
    new_day = None

    context = {
        "day_form":day_form,
        "new_day":new_day,
    }

    return(request, 'days/add-day.html', context)
