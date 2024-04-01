from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from booking.models import Booking
from .forms import BookingEditForm

@login_required
def myaccount(request):
    user_bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')
    recent_booking = user_bookings.first() if user_bookings.exists() else None
    
    if request.method == 'POST':
        if 'edit_booking' in request.POST:
            form = BookingEditForm(request.POST, instance=recent_booking)
            if form.is_valid():
                form.save()
                return redirect('myaccount:myaccount')
        elif 'cancel_booking' in request.POST and recent_booking:
            
            recent_booking.delete()
            return redirect('myaccount:myaccount')
    else:
        form = BookingEditForm(instance=recent_booking)

    return render(request, 'account.html', {
        'user_bookings': user_bookings,
        'recent_booking': recent_booking,
        'form': form
    })
