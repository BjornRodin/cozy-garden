# Generated by Django 3.2.22 on 2023-10-14 19:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20231010_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowers',
            name='favorites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
