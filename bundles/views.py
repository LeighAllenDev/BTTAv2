from django.shortcuts import render
from .models import Bundle
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
        # Simplify the response for demonstration purposes
        response = {
            "id": bundle.id,
            "food_categories": [{"id": cat.id, "name": cat.name} for cat in bundle.food_categories.all()],
            "drink_categories": [{"id": cat.id, "name": cat.name} for cat in bundle.drink_categories.all()],
        }
        return JsonResponse(response)
    except Bundle.DoesNotExist:
        return JsonResponse({'error': 'Bundle not found'}, status=404)