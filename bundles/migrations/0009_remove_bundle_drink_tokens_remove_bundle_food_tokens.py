# Generated by Django 4.2.10 on 2024-03-27 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bundles', '0008_remove_bundle_categories_remove_bundle_total_tokens_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bundle',
            name='drink_tokens',
        ),
        migrations.RemoveField(
            model_name='bundle',
            name='food_tokens',
        ),
    ]
