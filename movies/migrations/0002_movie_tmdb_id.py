# Generated by Django 4.2.16 on 2024-12-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tmdb_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
