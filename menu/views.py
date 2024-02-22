from django.shortcuts import render
from .models import Category

def menu(request):
    categories = Category.objects.prefetch_related('menuitems__options').all()
    categories = Category.objects.exclude(name='Default Category')
    return render(request, 'menu/menu.html', {'categories': categories})
