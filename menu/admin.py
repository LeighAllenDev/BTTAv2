from django.contrib import admin
from .models import Category, MenuItem, MenuItemOption

class MenuItemOptionInline(admin.TabularInline):
    model = MenuItemOption
    extra = 1  # Adjust if you want more or fewer empty forms

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
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
