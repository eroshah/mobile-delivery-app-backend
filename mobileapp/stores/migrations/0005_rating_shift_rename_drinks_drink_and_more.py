# Generated by Django 4.1.7 on 2023-02-20 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_remove_toppings_store_toppings_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('comment', models.TextField(max_length=120)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.store')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=36)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.store')),
            ],
        ),
        migrations.RenameModel(
            old_name='Drinks',
            new_name='Drink',
        ),
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]