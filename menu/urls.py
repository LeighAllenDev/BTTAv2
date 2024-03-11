from django.urls import path
from .views import menu_items_api, menu

urlpatterns = [
    path('', menu, name='menu'),
    path('api/menu-items/<int:category_id>/', menu_items_api, name='menu-items-api'),
]