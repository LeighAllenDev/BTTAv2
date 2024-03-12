from django.shortcuts import render
from .models import Bundle
from menu.models import MenuItem
from django.http import JsonResponse

# Create your views here. 
def bundles(request):
    # Prefetch related categories to reduce the number of database queries
    bundles = Bundle.objects.prefetch_related('food_categories', 'drink_categories').all()
    return render(request, "bundles/bundles.html", {'bundles': bundles})

def bundle_list(request):
    bundles = Bundle.objects.all()
    # Manually create the list of bundles data
    bundles_data = [{
        'id': bundle.id,
        'name': bundle.name,
        'description': bundle.description,
        # Add other necessary fields here
    } for bundle in bundles]
    
    return JsonResponse({'bundles': bundles_data})

def bundle_detail(request, pk):
    try:
        bundle = Bundle.objects.get(pk=pk)
        food_category_ids = bundle.food_categories.values_list('id', flat=True)
        drink_category_ids = bundle.drink_categories.values_list('id', flat=True)

        # Filter MenuItems for food and drinks based on the category IDs
        food_items = MenuItem.objects.filter(category__in=food_category_ids)
        drink_items = MenuItem.objects.filter(category__in=drink_category_ids)

        # Simplify the response for demonstration purposes
        response = {
            "id": bundle.id,
            "food_categories": [{"id": cat.id, "name": cat.name} for cat in bundle.food_categories.all()],
            "drink_categories": [{"id": cat.id, "name": cat.name} for cat in bundle.drink_categories.all()],
            "food_items": [{"id": item.id, "name": item.name, "category_id": item.category_id} for item in food_items],
            # Assuming you also want to include drink_items in the response
            "drink_items": [{"id": item.id, "name": item.name, "category_id": item.category_id} for item in drink_items],
        }
        return JsonResponse(response)
    except Bundle.DoesNotExist:
        return JsonResponse({'error': 'Bundle not found'}, status=404)