# Generated by Django 4.2.16 on 2024-12-09 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0004_alter_watchlist_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='note',
        ),
    ]
