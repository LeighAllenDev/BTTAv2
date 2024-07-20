from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from booking.models import Booking

@login_required
def myaccount_view(request):
    user_bookings = Booking.objects.filter(user=request.user)

    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        if booking_id:
            booking = get_object_or_404(Booking, id=booking_id, user=request.user)
            if 'cancel_booking' in request.POST:
                booking.delete()
                messages.success(request, 'Booking canceled successfully!')
                return redirect('myaccount:myaccount')
    
    return render(request, 'account.html', {
        'user_bookings': user_bookings,
    })

@login_required
def cancel_booking_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking canceled successfully!')
        return redirect('myaccount:myaccount')
    
    # Handle non-POST requests here if necessary (e.g., show a confirmation page)
    return redirect('myaccount:myaccount')
