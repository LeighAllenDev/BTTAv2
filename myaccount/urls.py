from django.urls import path
from . import views

app_name = 'myaccount'

urlpatterns = [
    path('', views.myaccount_view, name='myaccount'),
     path('cancel/<int:booking_id>/', views.cancel_booking_view, name='cancel_booking'),
]

