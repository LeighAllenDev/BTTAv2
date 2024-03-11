from django.db import models
from menu.models import Category, MenuItem

class Bundle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    food_categories = models.ManyToManyField(Category, related_name='food_bundle', limit_choices_to={'type': 'food'}, blank=True)
    drink_categories = models.ManyToManyField(Category, related_name='drink_bundle', limit_choices_to={'type': 'drink'}, blank=True)
    food_tokens = models.IntegerField(default=0, help_text="Total food tokens available for this bundle")
    drink_tokens = models.IntegerField(default=0, help_text="Total drink tokens available for this bundle")
    number_of_people = models.IntegerField(default=1)
    playtime_hours = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name