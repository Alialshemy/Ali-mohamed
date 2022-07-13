# Generated by Django 4.0.4 on 2022-07-10 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain
import profiles.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='stuff',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('image', models.ImageField(upload_to=profiles.models.get_file_path)),
                ('role', models.CharField(choices=[('seller', 'seller'), ('employe', 'employe'), ('manager', 'manager'), ('boss', 'boss')], max_length=50)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.store')),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='00000000000', max_length=11)),
                ('image', models.ImageField(upload_to=profiles.models.get_file_path)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('market_name', models.CharField(default='null', max_length=50)),
                ('address', models.CharField(default='null', max_length=50)),
                ('wallet_money', models.DecimalField(decimal_places=10, default=0, max_digits=20)),
                ('store_id', models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='Store.store')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]