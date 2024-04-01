from django.db import models

from .request import Request


class ChargeAccountRequest(Request):
    amount = models.FloatField(default=0)
    concept = models.CharField(max_length=200)
    costs_and_deductions = models.CharField(default='Not Set',max_length=200)
    rent_tax_declarant = models.BooleanField(default=True)
    fiscal_resident = models.BooleanField(default=False)
    city = models.CharField(default="Not Set", max_length=20)
    date = models.DateField(default="Not Set")
    bank_name = models.CharField(default="Not Set", max_length=20)
    account_type = models.CharField(default="Not Set", max_length=20)
    account_number = models.CharField(default="Not Set", max_length=20)
    cex_no = models.CharField(default="Not Set", max_length=20)

    def isRent_Tax_Declarant(self, element: bool):
        if element:
            self.rent_tax_declarant = True
        else:
            self.rent_tax_declarant = False

    def isFiscal_Resident(self, element: bool):
        if element:
            self.fiscal_resident = True
        else:
            self.fiscal_resident = False
