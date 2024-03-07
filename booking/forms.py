from django import forms
from .models import Booking
from menu.models import Category, MenuItem  # Assuming the Category model is in the menu app

class BookingForm(forms.ModelForm):
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
        if 'bundle' in self.initial:
            bundle = self.initial['bundle']
            # Assuming Bundle model has a relation to Category model (e.g., through ManyToManyField)
            # And Category model has a 'type' field distinguishing between 'food' and 'drink'
            food_categories = bundle.categories.filter(type='food')
            drink_categories = bundle.categories.filter(type='drink')
            self.fields['food_choice'].queryset = MenuItem.objects.filter(category__in=food_categories)
            self.fields['drink_choice'].queryset = MenuItem.objects.filter(category__in=drink_categories)
