# Generated by Django 4.1.7 on 2023-03-15 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0030_alter_rating_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 15, 19, 42, 3, 197802)),
        ),
    ]
