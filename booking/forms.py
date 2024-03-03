from django import forms
from .models import Booking
from menu.models import Category, MenuItem

class BookingForm(forms.ModelForm):
    # Assuming you have a way to identify menu items that could be part of a bundle
    food_choice = forms.ModelChoiceField(queryset=MenuItem.objects.none(), required=False)
    drink_choice = forms.ModelChoiceField(queryset=MenuItem.objects.none(), required=False)
    
    class Meta:
        model = Booking
        fields = ['bundle', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        # Dynamically set the queryset for food_choice and drink_choice if needed
        # This is a placeholder, actual implementation will depend on your models and requirements
        if 'initial' in kwargs:
            bundle = kwargs['initial'].get('bundle')
            if bundle:
                self.fields['food_choice'].queryset = MenuItem.objects.filter(bundle=bundle, type='food')
                self.fields['drink_choice'].queryset = MenuItem.objects.filter(bundle=bundle, type='drink')
