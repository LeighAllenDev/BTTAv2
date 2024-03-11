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
        # Manually create the bundle data
        bundle_data = {
            'id': bundle.id,
            'name': bundle.name,
            'description': bundle.description,
            'food_tokens': bundle.food_tokens,
            'drink_tokens': bundle.drink_tokens,
            # Include fields for categories, tokens etc. as needed
            # For related categories, you might need additional queries and processing
            'food_categories': list(bundle.food_categories.values('id', 'name')),
            'drink_categories': list(bundle.drink_categories.values('id', 'name')),
            # Assuming you have fields like food_tokens, drink_tokens in your model
        }
        
        return JsonResponse(bundle_data)
    except Bundle.DoesNotExist:
        return JsonResponse({'message': 'Bundle not found'}, status=404)  # Using Django's status code shortcut
        