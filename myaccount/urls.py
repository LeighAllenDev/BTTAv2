from django.urls import path
from . import views

app_name = 'myaccount'

urlpatterns = [
    path('', views.myaccount, name='myaccount'),
]

