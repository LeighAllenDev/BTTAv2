from django import forms
from .models import MenuItemOption

class MenuItemOptionForm(forms.ModelForm):
    class Meta:
        model = MenuItemOption
        fields = '__all__'
        widgets = {
            'size': forms.TextInput(attrs={'placeholder': 'Optional if only one size'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(MenuItemOptionForm, self).__init__(*args, **kwargs)
        self.fields['size'].required = False
