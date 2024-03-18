from django.db import models


class Format(models.Model):
    type = models.CharField(max_length=100)
    file = models.FileField(upload_to="formats/")


class RequestStatus(models.Model):
    status = models.CharField(max_length=100)


class RequestType(models.Model):
    type = models.CharField(max_length=100)


class ChargeAccountRequest(models.Model):
    user_name = models.CharField(default='Not Set',max_length=20)
    document_type = models.CharField(default='Not Set',max_length=20)
    user_id = models.CharField(max_length=30)
    amount = models.FloatField(default=0)
    concept = models.CharField(max_length=200)
    costs_and_deductions = models.BooleanField(default=True)
    rent_tax_declarant = models.BooleanField(default=True)
    fiscal_resident = models.BooleanField(default=False)
    city = models.CharField(default='Not Set',max_length=20)
    date = models.DateField(default='Not Set')
    bank_name = models.CharField(default='Not Set',max_length=20)
    account_type = models.CharField(default='Not Set',max_length=20)
    account_number = models.CharField(default='Not Set',max_length=20)
    CEX_no = models.CharField(default='Not Set',max_length=20)

    def isCost_and_Deductions(self,element:bool):
        if element:
            self.costs_and_deductions = True
        else:
            self.costs_and_deductions = False

    def isRent_Tax_Declarant(self,element:bool):
        if element:
            self.rent_tax_declarant = True
        else:
            self.rent_tax_declarant = False

    def isFiscal_Resident(self,element:bool):
        if element:
            self.fiscal_resident = True
        else:
            self.fiscal_resident = False



class Request(models.Model):
    type = models.ForeignKey(RequestType, on_delete=models.CASCADE)
    status = models.ForeignKey(RequestStatus, on_delete=models.CASCADE)
    requester = models.ForeignKey(
        "users_mgmt.CustomUser",
        on_delete=models.CASCADE,
        related_name="requested_requests",
    )
    manager = models.ForeignKey(
        "users_mgmt.CustomUser",
        on_delete=models.CASCADE,
        related_name="managed_requests",
        null=True,
        blank=True,
    )
    reviewer = models.ForeignKey(
        "users_mgmt.CustomUser",
        on_delete=models.CASCADE,
        related_name="reviewed_requests",
        null=True,
        blank=True,
    )
    approver = models.ForeignKey(
        "users_mgmt.CustomUser",
        on_delete=models.CASCADE,
        related_name="approved_requests",
        null=True,
        blank=True,
    )
    format = models.ForeignKey(Format, on_delete=models.CASCADE)
    initial_date = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateTimeField(null=True, blank=True)


class Documents(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    file = models.FileField(upload_to="documents/")
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
