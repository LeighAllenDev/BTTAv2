from django.contrib import admin
from django import forms
from .models import Category, MenuItem, MenuItemOption
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



class MenuItemOptionInline(admin.TabularInline):
    model = MenuItemOption
    extra = 1  # Adjust if you want more or fewer empty forms

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class MenuItemForm(forms.ModelForm):
        class Meta:
            model = MenuItem
            widgets = {
                'description': SummernoteWidget(),
            }
            fields = '__all__'

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm
    list_display = ['name', 'category', 'display_price_range']
    list_filter = ['category']
    inlines = [MenuItemOptionInline]

    def display_price_range(self, obj):
        options = obj.options.all()
        if options:
            min_price = min(option.price for option in options)
            max_price = max(option.price for option in options)
            if min_price != max_price:
                return f"£{min_price} - £{max_price}"
            return f"£{min_price}"
        return "N/A"
    display_price_range.short_description = 'Price Range'

    
