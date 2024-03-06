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
def menu_items_list(request, category_id=None):
    if category_id:
        menu_items = MenuItem.objects.filter(category__id=category_id)
    else:
        menu_items = MenuItem.objects.all()
    serializer = MenuItemSerializer(menu_items, many=True)
    return Response(serializer.data)