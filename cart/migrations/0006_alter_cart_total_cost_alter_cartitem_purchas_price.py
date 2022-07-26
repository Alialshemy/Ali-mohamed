# Generated by Django 4.0.4 on 2022-07-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_cartitem_purchas_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='purchas_price',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
    ]
