from django.urls import path
from . import views


app_name = 'booking'

urlpatterns = [
    path('', views.booking_view, name='booking'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]
