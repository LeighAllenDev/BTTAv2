from django.db import models
from menu.models import Category, MenuItem

class Bundle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Assuming a Category model that includes both food and drink categories
    food_categories = models.ManyToManyField(Category, related_name='food_bundle', limit_choices_to={'type': 'food'})
    drink_categories = models.ManyToManyField(Category, related_name='drink_bundle', limit_choices_to={'type': 'drink'})
    food_tokens = models.IntegerField(default=0)
    drink_tokens = models.IntegerField(default=0)
    number_of_people = models.IntegerField(default=1)
    playtime_hours = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
