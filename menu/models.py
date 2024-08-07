from django.db import models

def create_default_category():
    category, _ = Category.objects.get_or_create(name='Default Category')
    return category.pk

class Category(models.Model):
    CATEGORY_TYPES = (
        ('food', 'Food'),
        ('drink', 'Drink'),
    )
    name = models.CharField(max_length=100)
    token_cost = models.IntegerField(default=1, help_text="Token cost for each item in this category")
    type = models.CharField(max_length=5, choices=CATEGORY_TYPES, default='food', help_text='Specify whether this category is for food or drink.')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='menuitems', on_delete=models.CASCADE, default=create_default_category)

    def __str__(self):
        return self.name

class MenuItemOption(models.Model):
    menu_item = models.ForeignKey(MenuItem, related_name='options', on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.name} - {self.size} - £{self.price}"
