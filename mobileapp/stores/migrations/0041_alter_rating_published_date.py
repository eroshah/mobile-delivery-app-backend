# Generated by Django 4.1.7 on 2023-03-18 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0040_alter_rating_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]