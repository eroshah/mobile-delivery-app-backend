# Generated by Django 4.1.7 on 2023-03-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0041_alter_rating_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]