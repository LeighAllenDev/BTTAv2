from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from bundles.models import Bundle
import logging

logger = logging.getLogger(__name__)

@login_required
def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking:booking_confirmation', booking_id=booking.id)
        else:
            logger.error(f"Form errors: {form.errors}")
    else:
        bundle_id = request.GET.get('bundle')
        initial_data = {}
        if bundle_id:
            try:
                bundle = Bundle.objects.get(id=bundle_id)
                initial_data['bundle'] = bundle
            except Bundle.DoesNotExist:
                logger.error(f"Bundle with id {bundle_id} does not exist.")
                initial_data['bundle'] = None
        
        form = BookingForm(initial=initial_data)

    return render(request, 'booking.html', {'form': form})

@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_confirmation.html', {'booking': booking})
