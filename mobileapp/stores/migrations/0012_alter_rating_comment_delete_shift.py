# Generated by Django 4.1.7 on 2023-02-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0011_remove_store_days_of_week_alter_rating_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='comment',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
        migrations.DeleteModel(
            name='Shift',
        ),
    ]
