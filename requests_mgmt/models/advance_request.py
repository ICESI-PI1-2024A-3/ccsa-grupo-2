from django.db import models
from django.views import View

from .request import Request

class AdvanceRequest(Request):
    request_date = models.DateField(null=True,blank=True)
    dependency = models.CharField(default='Not Set',max_length=200)

    destination_city =models.CharField(default='Not Set',max_length=200)

    departure_date=models.DateField(null=True,blank=True)

    return_date=models.DateField(null=True,blank=True)

    reason_trip=models.CharField(default='Not Set',max_length=200)

    advance_currency = models.CharField(default='Not Set',max_length=200)

    icesi_last_day_date=models.DateField(null=True,blank=True)

    payment_order_code=models.CharField(default='Not Set',max_length=200)

    airport_transport = models.FloatField(default=0)
    local_transport = models.FloatField(default=0)
    feeding = models.FloatField(default=0)
    accommodation = models.FloatField(default=0)
    departure_taxes = models.FloatField(default=0)
    others = models.FloatField(default=0)
    
    widget = models.FloatField(default=0)

