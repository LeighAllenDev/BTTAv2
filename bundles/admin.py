from django.contrib import admin
from .models import Bundle
from menu.models import Category  # Assuming the Category model is from 'menu' app

class BundleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'number_of_people', 'playtime_hours')
    filter_horizontal = ('food_categories', 'drink_categories')

admin.site.register(Bundle, BundleAdmin)
