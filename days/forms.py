from django import forms
from trips.models import Trip, Destination, Resort
from .models import Day
from profile import Profile
from .utils import date_choices

class DayCreationForm(forms.Form):
    date = forms.DateField(input_formats=["%Y-%m-%d"], widget=forms.Select(choices=()))
    resort = forms.ModelChoiceField(queryset=Resort.objects.all())
    restaurant = forms.CharField(max_length=100)
    
    def __init__(self, *args, dest_pk=None, dates=None, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['resort'].queryset = Resort.objects.filter(destination=dest_pk)
        self.fields['date'].widget = forms.Select(choices=date_choices(dates))


class DayEditForm(forms.Form):
    date = forms.DateField(input_formats=["%Y-%m-%d"], widget=forms.Select(choices=()), initial=None)
    # date = forms.ChoiceField(choices=None)
    resort = forms.ModelChoiceField(queryset=Resort.objects.all())
    restaurant = forms.CharField(max_length=100)
    
    def __init__(self, *args, dest_pk=None, dates=None, initial_date=None, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.Select(choices=date_choices(dates))
        self.fields['resort'].queryset = Resort.objects.filter(destination=dest_pk)
        # self.fields['date'].choices = date_choices(dates)


