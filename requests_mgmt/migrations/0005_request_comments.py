# Generated by Django 5.0.3 on 2024-03-30 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests_mgmt', '0004_alter_request_type_alter_request_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
