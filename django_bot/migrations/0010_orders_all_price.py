# Generated by Django 4.1.7 on 2023-07-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_bot', '0009_alter_orders_cake_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='all_price',
            field=models.IntegerField(default=0, verbose_name='Общая стоимость'),
        ),
    ]