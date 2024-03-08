# Generated by Django 4.2.10 on 2024-03-08 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_category_type'),
        ('bundles', '0005_remove_bundle_categories_bundle_total_tokens'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='bundles', to='menu.category'),
        ),
    ]
