# Generated by Django 3.1 on 2024-09-23 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_auto_20240923_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='category_slug',
        ),
    ]
