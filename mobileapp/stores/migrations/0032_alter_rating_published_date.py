# Generated by Django 4.1.7 on 2023-03-17 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0031_alter_rating_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 0, 52, 59, 929923)),
        ),
    ]