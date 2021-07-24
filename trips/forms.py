from django import forms
from .models import Trip, Destination
from profiles.models import Profile

DESTINATION_CHOICES = (
    ('#1', 'Salt Lake City'),
    ('#2', 'Rockies'),
    ('#3', 'Southern Colorado/New Mexico'),
    ('#4', 'Wyoming'),
    ('#5', 'Montana'),
    ('#6', 'British Columbia'),
    ('#7', 'California'),
    ('#8', 'Idaho'),
)


class TripCreationForm(forms.Form):
    trip_name = forms.CharField(max_length=200)
    date_arrived = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    date_departed = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    hotel = forms.CharField(max_length=200)
    user = forms.ModelChoiceField(queryset=Profile.objects.all())
    destination = forms.ModelChoiceField(queryset=Destination.objects.all())
