from django.shortcuts import redirect, render
from django.views import View

from ..forms import (
    InvoiceLegalizationForm,
    ExpenseRatioForm
)
# from ..models import 

class InvoiceLegalizationView(View):
    template_name = "requests/create_invoice_legalization_request.html"
    invoice_legalization_form = InvoiceLegalizationForm
    expense_ratio_form = ExpenseRatioForm


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "invoice_legalization_form": self.invoice_legalization_form(),
            "expense_ratio_form": self.expense_ratio_form(),
        })