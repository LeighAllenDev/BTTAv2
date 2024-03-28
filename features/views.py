from django.shortcuts import render

# Create your views here.
def features(request):
    template_name = "features.html"
    return render(request, template_name)