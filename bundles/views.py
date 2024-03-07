from django.shortcuts import render
from .models import Bundle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BundleSerializer

# Create your views here.
def bundles(request):
    bundles = Bundle.objects.prefetch_related('categories').all()
    template_name = "bundles/bundles.html"
    return render(request, template_name, {'bundles': bundles})


@api_view(['GET'])
def bundle_detail(request, pk):
    try:
        bundle = Bundle.objects.get(pk=pk)
        serializer = BundleSerializer(bundle)
        return Response(serializer.data)
    except Bundle.DoesNotExist:
        return Response({'error': 'Bundle not found'}, status=404)