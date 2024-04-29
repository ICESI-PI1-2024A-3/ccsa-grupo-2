from django.db import models

from .request import Request


class Expense(models.Model):
    rubro = models.CharField(max_length=200, default='Not Set')
    request_id_number = models.ForeignKey("Request",on_delete=models.CASCADE, default=1)
    proveedor = models.CharField(max_length=200, default='Not Set')
    nit = models.CharField(max_length=200, default='Not Set')
    concepto = models.CharField(max_length=200, default='Not Set')
    advance_currency = models.CharField(max_length=200, default='Not Set')
    amount = models.DecimalField(default=0,decimal_places=2,max_digits=10)
    coment = models.CharField(max_length=200, default='Not Set')