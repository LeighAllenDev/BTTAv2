from django.db import models
from django.conf import settings
from bundles.models import Bundle
from menu.models import MenuItem
from django.utils import timezone

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bundle = models.ForeignKey(Bundle, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    time = models.TimeField()
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Booking for {self.user} on {self.date} at {self.time}"

    @property
    def total_tokens_used(self):
        """Calculate total tokens used for both food and drink."""
        return self.food_tokens_used + self.drink_tokens_used

    def check_token_allocation(self):
        """Method to check if the selected items exceed the available tokens in the selected bundle.
        This could be implemented to automatically validate upon booking save or as a manual method to call."""
        if self.bundle:
            total_food_tokens_available = self.bundle.food_tokens
            total_drink_tokens_available = self.bundle.drink_tokens

            total_food_tokens_used = sum([item.token_cost for item in self.food_items.all()])
            total_drink_tokens_used = sum([item.token_cost for item in self.drink_items.all()])

            self.food_tokens_used = total_food_tokens_used
            self.drink_tokens_used = total_drink_tokens_used

            if total_food_tokens_used > total_food_tokens_available or total_drink_tokens_used > total_drink_tokens_available:
                return False  
            return True
