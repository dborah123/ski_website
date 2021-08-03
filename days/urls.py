from django.urls import path
from .views import (
    add_day_view,
)

app_name = "days"

urlpatterns = [
    path('add_day/<pk>', add_day_view, name="add-day")
]