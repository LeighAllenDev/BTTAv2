from django.shortcuts import render
from .models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer

def menu(request):
    categories = Category.objects.prefetch_related('menuitems__options').all()
    categories = Category.objects.exclude(name='Default Category')
    return render(request, 'menu/menu.html', {'categories': categories})


@api_view(['GET'])
def menu_items_json(request):
    food_items = MenuItem.objects.filter(category__type='food')
    drink_items = MenuItem.objects.filter(category__type='drink')
    food_serializer = MenuItemSerializer(food_items, many=True)
    drink_serializer = MenuItemSerializer(drink_items, many=True)
    
    return Response({
        'food_items': food_serializer.data,
        'drink_items': drink_serializer.data
    })