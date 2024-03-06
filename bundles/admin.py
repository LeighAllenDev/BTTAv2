# bundles/admin.py

from django.contrib import admin
from .models import Bundle
from django.forms import CheckboxSelectMultiple
from django.db import models

class BundleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Bundle, BundleAdmin)
