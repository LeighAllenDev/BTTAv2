from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from bundles.models import Bundle
import logging


logger = logging.getLogger(__name__)

@login_required
def booking_view(request):
    initial_data = {}
    bundle_id = request.POST.get('bundle') if request.method == 'POST' else request.GET.get('bundle')
    if bundle_id:
        try:
            initial_data['bundle'] = Bundle.objects.get(id=bundle_id)
        except Bundle.DoesNotExist:
            initial_data['bundle'] = None

    if request.method == 'POST':
        form = BookingForm(request.POST, initial=initial_data)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking:booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm(initial=initial_data)

    return render(request, 'booking.html', {'form': form})

@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_confirmation.html', {'booking': booking})
