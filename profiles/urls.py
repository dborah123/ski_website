from django.urls import path
from .views import (
    my_profile_view,
    home_view
)

app_name = 'profiles'

urlpatterns = [
    path('my-profile', my_profile_view, name='main'),
    path('', home_view, name='home'),
]