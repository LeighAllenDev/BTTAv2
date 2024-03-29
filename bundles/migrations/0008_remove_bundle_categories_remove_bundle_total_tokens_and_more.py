# Generated by Django 4.2.10 on 2024-03-10 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_category_type'),
        ('bundles', '0007_remove_bundle_drink_categories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bundle',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='bundle',
            name='total_tokens',
        ),
        migrations.AddField(
            model_name='bundle',
            name='drink_categories',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 'drink'}, related_name='drink_bundle', to='menu.category'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='drink_tokens',
            field=models.IntegerField(default=0, help_text='Total drink tokens available for this bundle'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='food_categories',
            field=models.ManyToManyField(blank=True, limit_choices_to={'type': 'food'}, related_name='food_bundle', to='menu.category'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='food_tokens',
            field=models.IntegerField(default=0, help_text='Total food tokens available for this bundle'),
        ),
    ]
