# api_views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from bundles.models import Bundle

@api_view(['GET'])
def bundle_detail_api(request, pk):
    try:
        bundle = Bundle.objects.get(pk=pk)
        # Example of manually building the response
        response_data = {
            'name': bundle.name,
            'description': bundle.description,
            # Add other fields as needed
        }
        return Response(response_data)
    except Bundle.DoesNotExist:
        return Response({'error': 'Bundle not found'}, status=404)
