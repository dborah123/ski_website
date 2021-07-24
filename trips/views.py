from django.shortcuts import render
from .forms import TripCreationForm

# Create your views here.

def home_view(request):
    trip_form = TripCreationForm(request.POST or None)


    context = {
        'trip_form':trip_form,
    }

    return render(request, 'trips/home.html', context)