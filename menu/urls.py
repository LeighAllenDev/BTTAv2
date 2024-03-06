from . import views
from django.urls import path
from .views import menu_items_list

urlpatterns = [
    path('', views.menu, name='menu'),
    path('api/menu-items/', menu_items_list, name='api-menu-items'),
]