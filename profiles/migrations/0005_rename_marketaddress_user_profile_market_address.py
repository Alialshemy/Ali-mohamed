# Generated by Django 4.0.4 on 2022-07-16 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_user_profile_marketname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='marketAddress',
            new_name='market_address',
        ),
    ]
