from django.shortcuts import render

# Create your views here.
def menu(request):
    template_name = "menu/menu.html"
    return render(request, template_name)