# Generated by Django 3.2.9 on 2021-12-11 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_rename_is_activate_cartitem_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='variation',
            new_name='variations',
        ),
    ]
