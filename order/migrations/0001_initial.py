# Generated by Django 4.0.4 on 2022-07-25 08:11

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain
import order.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Store', '0001_initial'),
        ('product', '0001_initial'),
        ('profiles', '0006_alter_user_profile_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=40, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('purchas_price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('profit', models.DecimalField(decimal_places=10, max_digits=20)),
                ('sellin_price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('markert_name', models.CharField(max_length=30)),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_image', models.ImageField(upload_to=order.models.get_file_path)),
                ('market_address', models.CharField(max_length=30)),
                ('customer_location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.user_profile')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.store')),
            ],
        ),
        migrations.CreateModel(
            name='orderitem',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=40, primary_key=True, serialize=False)),
                ('selling_price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('quantity', models.IntegerField()),
                ('list_amount', models.DecimalField(decimal_places=10, max_digits=20)),
                ('list_selling', models.DecimalField(decimal_places=10, max_digits=20)),
                ('purchase_price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('is_unit', models.BooleanField()),
                ('product_image', models.ImageField(upload_to=order.models.get_file_path)),
                ('product_title', models.CharField(max_length=30)),
                ('product_name', models.CharField(max_length=30)),
                ('unit_name', models.CharField(max_length=30)),
                ('list_name', models.CharField(max_length=30)),
                ('total_purchase', models.DecimalField(decimal_places=10, max_digits=20)),
                ('total_selling_price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('profit', models.DecimalField(decimal_places=10, max_digits=20)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
