from . import views
from django.urls import path
from .views import menu_items_json

urlpatterns = [
    path('', views.menu, name='menu'),
    path('api/menu-items/', menu_items_json, name='api-menu-json'),
]