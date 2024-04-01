from django.db import models

from .request import Request


class AdvanceRequest(Request):
    request_date = models.DateField(default='2000-01-01')
    dependency = models.CharField(default='Not Set',max_length=200)

    destination_city =models.CharField(default='Not Set',max_length=200)

    departure_date=models.DateField(default='2000-01-01')

    return_date=models.DateField(default='2000-01-01')

    reason_trip=models.CharField(default='Not Set',max_length=200)

    advance_currency = models.CharField(default='Not Set',max_length=200)

    icesi_last_date=models.DateField(null=True,blank=True)

    payment_order_code=models.CharField(default='Not Set',max_length=200)

    airport_transport = models.FloatField(default=0)
    local_transport = models.FloatField(default=0)
    food_expense = models.FloatField(default=0)
    alojamiento = models.FloatField(default=0)
    other_expenses = models.FloatField(default=0)

    advance_total = models.FloatField(default=0)
