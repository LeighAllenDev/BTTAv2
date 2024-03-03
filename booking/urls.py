from django.urls import path
from .views import booking_view  # Ensure you're importing the correct view function

urlpatterns = [
    path('booking/', booking_view, name='booking'),  # Use booking_view here
]
