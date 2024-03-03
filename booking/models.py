from django.db import models
from django.conf import settings
from bundles.models import Bundle

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bundle = models.ForeignKey(Bundle, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    # Add any additional fields as needed

    def __str__(self):
        return f"Booking for {self.user} on {self.date} at {self.time}"
