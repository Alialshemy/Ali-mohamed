# Generated by Django 4.0.4 on 2022-07-26 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_listselling_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='listselling_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_cost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.FloatField(),
        ),
    ]