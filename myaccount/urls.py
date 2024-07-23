from django.urls import path
from . import views

app_name = 'myaccount'

urlpatterns = [
    path('', views.myaccount_view, name='myaccount'),
    path('edit/<int:booking_id>/', views.edit_booking_view, name='edit_booking'),
]