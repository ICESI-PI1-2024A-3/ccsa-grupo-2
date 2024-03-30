from django.db import models

from . import (
    AdvanceRequest,
    ChangeAccountRequest,
    InvoiceLegalizationRequest,
    TravelExpenseRequest,
)


class RequestType(models.Model):
    type = models.ForeignKey(
        ChangeAccountRequest
        or AdvanceRequest
        or InvoiceLegalizationRequest
        or TravelExpenseRequest,
        on_delete=models.CASCADE,
    )
