from django.shortcuts import render

# Create your views here.
def bundles(request):
    template_name = "bundles/bundles.html"
    return render(request, template_name)