# Generated by Django 5.0.3 on 2024-05-13 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Role',
            new_name='Roles',
        ),
    ]
