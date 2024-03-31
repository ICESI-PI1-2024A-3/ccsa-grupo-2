from django.shortcuts import render
from django.views import View

from ..models import (
    AdvanceRequest,
    ChargeAccountRequest,
    InvoiceLegalizationRequest,
    TravelExpenseRequest,
)


class RequestsListView(View):
    template_name = "requests_list.html"

    def get(self, request):
        requests = {
            "advance": AdvanceRequest.objects.all(),
            "charge_account": ChargeAccountRequest.objects.all(),
            "invoice_legalization": InvoiceLegalizationRequest.objects.all(),
            "travel_expense": TravelExpenseRequest.objects.all(),
        }
        return render(request, self.template_name, requests)
