# Generated by Django 5.0.3 on 2024-04-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests_mgmt', '0010_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='coment',
            field=models.CharField(default='Not Set', max_length=200),
        ),
    ]
