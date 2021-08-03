from django.urls import path
from .views import (
    home_view,
    trips_view,
    trip_details_view,
)

app_name = 'trips'

urlpatterns = [
    path('', home_view, name='home'),
    path('trips/', trips_view, name='trips'),
    path('trips/<pk>', trip_details_view, name='detail'),
]