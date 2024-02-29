from django import forms
from .models import Bundle, Category, Drink

class BundleForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    drinks = forms.ModelMultipleChoiceField(queryset=Drink.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Bundle
        fields = ['name', 'food_tokens', 'drink_tokens', 'categories', 'drinks', 'number_of_people', 'playtime_hours']
