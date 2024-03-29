from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from bundles.models import Bundle  # Ensure this import is correct based on your project structure

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
            # Save the booking instance to generate an ID
            booking.save()
            return redirect('accounts:view_account')
        else:
            pass 
            
    else:
        form = BookingForm(initial=initial_data)

    return render(request, 'booking.html', {'form': form})