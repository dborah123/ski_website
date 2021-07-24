from django.db import models
from django.utils import timezone
from profiles.models import Profile

# Create your models here.

class Destination(models.Model):
    location = models.CharField(max_length = 200)

    def __str__(self):
        return self.location

class Trip(models.Model):
    trip_name = models.CharField(max_length=50, blank=True)
    date_arrived = models.DateField(blank=True, null=True)
    date_departed = models.DateField(blank=True, null=True)
    hotel = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)


    def __str__(self):
        return self.trip_name

