from django.shortcuts import render
from .models import Category, MenuItem
from django.http import JsonResponse

def menu(request):
    # Combine prefetch_related and exclude in a single query
    categories = Category.objects.exclude(name='Default Category').prefetch_related('menuitems__options')
    return render(request, 'menu/menu.html', {'categories': categories})

def menu_items_api(request, category_id=None):
    if category_id:
        menu_items = MenuItem.objects.filter(category_id=category_id)
    else:
        menu_items = MenuItem.objects.all()
    
    items = [{"id": item.id, "name": item.name} for item in menu_items]
    return JsonResponse({"menu_items": items})
