from django import forms
from .models import Trip, Destination
from profiles.models import Profile


class TripCreationForm(forms.Form):
    trip_name = forms.CharField(max_length=200)
    date_arrived = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    date_departed = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    hotel = forms.CharField(max_length=200)
    user = forms.ModelChoiceField(queryset=Profile.objects.all())
    destination = forms.ModelChoiceField(queryset=Destination.objects.all())
