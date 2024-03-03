from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required  # If you want to require users to be logged in

@login_required  # Remove this if you don't want to require login
def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            # Redirect to a confirmation page or similar
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})  # Note the corrected template path here
