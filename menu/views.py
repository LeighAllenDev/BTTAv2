from django.shortcuts import render
from .models import Category, MenuItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MenuItemSerializer

def menu(request):
    # Combine prefetch_related and exclude in a single query
    categories = Category.objects.exclude(name='Default Category').prefetch_related('menuitems__options')
    return render(request, 'menu/menu.html', {'categories': categories})

@api_view(['GET'])
def menu_items_json(request):
    # Your API view seems correctly set up to provide serialized data for food and drink items
    food_items = MenuItem.objects.filter(category__type='food')
    drink_items = MenuItem.objects.filter(category__type='drink')
    food_serializer = MenuItemSerializer(food_items, many=True)
    drink_serializer = MenuItemSerializer(drink_items, many=True)
    
    return Response({
        'food_items': food_serializer.data,
        'drink_items': drink_serializer.data
    })
