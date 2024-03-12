from django import forms
from .models import Booking
from menu.models import MenuItem  # Import other necessary models

class BookingForm(forms.ModelForm):
    # Assuming you already have these fields defined
    food_choice = forms.ModelChoiceField(queryset=MenuItem.objects.none(), required=False)
    drink_choice = forms.ModelChoiceField(queryset=MenuItem.objects.none(), required=False)

    class Meta:
        model = Booking
        fields = ['bundle', 'date', 'time', 'food_choice', 'drink_choice']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        if 'initial' in kwargs and 'bundle' in kwargs['initial']:
            bundle = kwargs['initial']['bundle']
            self.fields['food_choice'].queryset = MenuItem.objects.filter(category__in=bundle.food_categories.all())
            self.fields['drink_choice'].queryset = MenuItem.objects.filter(category__in=bundle.drink_categories.all())
