from django.contrib import admin
from .models import Booking
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'bundle', 'date', 'time')
    list_filter = ('bundle', 'date', 'user')
    search_fields = ('user__username', 'bundle__name')

    def display_food_items(self, obj):
        return self.display_items(obj.food_items.all())
    
    def display_drink_items(self, obj):
        return self.display_items(obj.drink_items.all())

    def display_items(self, items):
        # Display the items as a comma-separated list with token costs if available
        items_list = format_html_join(
            mark_safe('<br>'), 
            "{} ({} tokens)", 
            ((item.name, item.category.token_cost) for item in items)  # Assumes MenuItem has a name and is related to a Category with token_cost
        ) or mark_safe("<span class='errors'>No items selected</span>")
        return items_list

    display_food_items.short_description = "Food Items"
    display_drink_items.short_description = "Drink Items"

admin.site.register(Booking, BookingAdmin)
