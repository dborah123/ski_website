from django import forms
from trips.models import Trip, Destination, Resort
from profile import Profile

class DayCreationForm(forms.Form):
    date = forms.DateField()
    resort = None
    restaurant = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        pk = kwargs.get("pk")
        super(DayCreationForm, self).__init__(*args, **kwargs)

        if(pk):
            self.resort = forms.ModelChoiceField(queryset=Resort.objects.filter(Destination.objects.get(pk=pk)))