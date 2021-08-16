from django.urls import path
from .views import (
    trip_create_view,
    trips_view,
    trip_details_view,
)

app_name = 'trips'

urlpatterns = [
    path('', trip_create_view, name='create'),
    path('trips/', trips_view, name='trips'),
    path('trips/<pk>', trip_details_view, name='detail'),
]