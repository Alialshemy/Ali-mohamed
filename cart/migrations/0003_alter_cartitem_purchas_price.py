# Generated by Django 4.0.4 on 2022-07-23 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cartitem_purchas_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='purchas_price',
            field=models.FloatField(),
        ),
    ]