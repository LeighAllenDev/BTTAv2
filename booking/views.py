from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required  

@login_required 
def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})  