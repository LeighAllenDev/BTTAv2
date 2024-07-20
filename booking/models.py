from django.db import models
from bundles.models import Bundle
from django.contrib.auth.models import User
from django.utils import timezone

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bundle = models.ForeignKey(Bundle, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(default=timezone.localdate)
    time = models.TimeField(default=timezone.localtime)

    def __str__(self):
        return f"{self.bundle} - {self.date} at {self.time}"
