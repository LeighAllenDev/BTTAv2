from django import forms
from .models import Booking
from bundles.models import Bundle
from django.core.exceptions import ValidationError
from django.utils import timezone

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['bundle', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'step':'60'})  # 300 seconds = 5 minutes
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # If the instance is not saved yet
            self.fields['date'].initial = timezone.localdate()
        self.fields['bundle'].queryset = Bundle.objects.all()  # Ensure queryset for the bundle field

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date:
            today = timezone.localdate()
            if date <= today:
                raise ValidationError("Bookings cannot be made for today. Please select a future date.")
        return date

    def clean_time(self):
        time = self.cleaned_data.get('time')
        if time:
            opening_time = timezone.datetime.strptime("09:00", "%H:%M").time()
            closing_time = timezone.datetime.strptime("22:00", "%H:%M").time()
            if not (opening_time <= time <= closing_time):
                raise ValidationError("Bookings can only be made between 9 AM and 10 PM.")
            return time.replace(second=0, microsecond=0)  # Strip seconds
        return time

    def clean_bundle(self):
        bundle = self.cleaned_data.get('bundle')
        if bundle and not Bundle.objects.filter(id=bundle.id).exists():
            raise ValidationError("The selected bundle does not exist.")
        return bundle
