# Generated by Django 4.0.4 on 2022-07-22 17:56

import cart.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('Store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=40, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total_cost', models.DecimalField(decimal_places=10, max_digits=20)),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.store')),
            ],
        ),
        migrations.CreateModel(
            name='cartitem',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=40, primary_key=True, serialize=False)),
                ('purchas_price', models.FloatField()),
                ('quantity', models.BigIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('unitname', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=cart.models.get_file_path)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
