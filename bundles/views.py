from django.shortcuts import render
from .models import Bundle

# Create your views here.
def bundles(request):
    bundles = Bundle.objects.all()
    template_name = "bundles/bundles.html"
    return render(request, template_name, {'bundles': bundles})