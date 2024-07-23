from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from booking.forms import BookingForm
from booking.models import Booking
from django.contrib import messages

@login_required
def myaccount_view(request):
    # Retrieve all bookings for the logged-in user
    user_bookings = Booking.objects.filter(user=request.user)
    recent_booking = user_bookings.first() if user_bookings else None

    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)

        # Handle booking cancellation
        if 'cancel_booking' in request.POST:
            booking.delete()
            messages.success(request, 'Booking canceled successfully!')
            return redirect('myaccount:myaccount')

    return render(request, 'account.html', {
        'user_bookings': user_bookings,
        'recent_booking': recent_booking,
    })

@login_required
def edit_booking_view(request, booking_id):
    # Fetch the booking object for the logged-in user
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()  # Save the updated booking
            messages.success(request, 'Booking updated successfully!')
            return redirect('myaccount:myaccount')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'edit_booking.html', {'form': form, 'booking': booking})
