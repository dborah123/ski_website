from django.db import models
from trips.models import Trip, Destination, Resort
from django.utils import timezone
from profiles.models import Profile


# Create your models here.

class Day(models.Model):
    date = models.DateField(blank=True, null=True)
    ski_area = models.ForeignKey(Resort, on_delete=models.CASCADE)
    restaurant = models.CharField(max_length=100, blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete =models.CASCADE)

    def __str__(self):
        return str(self.date)
    