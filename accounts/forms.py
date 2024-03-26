from django import forms
from booking.models import Booking

class BookingEditForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
