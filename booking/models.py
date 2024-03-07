from django.db import models
from django.conf import settings
from bundles.models import Bundle
from menu.models import MenuItem

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bundle = models.ForeignKey(Bundle, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    food_items = models.ManyToManyField(MenuItem, related_name="booking_food_items", blank=True)
    drink_items = models.ManyToManyField(MenuItem, related_name="booking_drink_items", blank=True)
    # Additional fields for tokens if needed
    
    def __str__(self):
        return f"Booking for {self.user} on {self.date} at {self.time}"

    # Optionally, add methods to check token allocation if implementing a token system

