from django.shortcuts import render

# Create your views here.
def booking(request):
    template_name = "/workspace/BTTAv2/templates/booking.html"
    return render(request, template_name)