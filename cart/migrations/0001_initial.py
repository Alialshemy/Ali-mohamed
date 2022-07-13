# Generated by Django 4.0.4 on 2022-07-10 19:22

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
                ('date', models.DateField()),
                ('purchas_price', models.DecimalField(decimal_places=10, max_digits=20)),
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
                ('remaining', models.BigIntegerField()),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]