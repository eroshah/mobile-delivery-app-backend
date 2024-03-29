# Generated by Django 4.1.7 on 2023-02-25 12:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0009_alter_item_cuisine_alter_item_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='days_of_week',
            field=models.CharField(choices=[('SUN', 'Sunday'), ('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THURS', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday')], default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
