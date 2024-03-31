# Generated by Django 5.0.3 on 2024-03-31 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests_mgmt', '0006_alter_chargeaccountrequest_costs_and_deductions'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicelegalizationrequest',
            name='account_number',
            field=models.CharField(default='Not Set', max_length=20),
        ),
        migrations.AddField(
            model_name='invoicelegalizationrequest',
            name='account_type',
            field=models.CharField(default='Not Set', max_length=20),
        ),
        migrations.AddField(
            model_name='invoicelegalizationrequest',
            name='bank_name',
            field=models.CharField(default='Not Set', max_length=20),
        ),
        migrations.AddField(
            model_name='invoicelegalizationrequest',
            name='departure_date',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='invoicelegalizationrequest',
            name='dependency',
            field=models.CharField(default='Not Set', max_length=200),
        ),
        migrations.AddField(
            model_name='invoicelegalizationrequest',
            name='destination_city',
            field=models.CharField(default='Not Set', max_length=200),
        ),
        migrations.AddField(
            model_name='invoicelegalizationrequest',
            name='discount_authorization',
            field=models.CharField(default='Not Set', max_length=5),
        ),
        migrations.AddField(
            model_name='invoicelegalizationrequest',
            name='legalization_date',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='invoicelegalizationrequest',
            name='reason_trip',
            field=models.CharField(default='Not Set', max_length=200),
        ),
    ]
