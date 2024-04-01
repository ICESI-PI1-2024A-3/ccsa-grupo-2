from django.db import models

from .request import Request


class InvoiceLegalizationRequest(Request):
    legalization_date = models.DateField(default='2000-01-01')
    dependency = models.CharField(default='Not Set',max_length=200)

    destination_city =models.CharField(default='Not Set',max_length=200)

    departure_date=models.DateField(default='2000-01-01')

    reason_trip=models.CharField(default='Not Set',max_length=200)

    discount_authorization = models.CharField(default='Not Set',max_length=5)

    bank_name = models.CharField(default="Not Set", max_length=20)
    account_type = models.CharField(default="Not Set", max_length=20)
    account_number = models.CharField(default="Not Set", max_length=20)

