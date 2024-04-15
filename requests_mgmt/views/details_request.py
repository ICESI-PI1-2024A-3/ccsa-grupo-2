from django.shortcuts import render
from django.views import View

from ..forms import AddApproverForm, AddReviewerForm
from ..models import ChargeAccountRequest, InvoiceLegalizationRequest, Request


class DetailsRequestView(View):
    template_name = "request_details.html"
    select_reviewer_form = AddReviewerForm
    select_approver_form = AddApproverForm

    def get(self, request, request_id, *args, **kwargs):
        intance_request = Request.objects.get(pk=request_id)

        self.select_reviewer_form = AddReviewerForm(
            selected_reviewer_id=(
                intance_request.reviewer.id if intance_request.reviewer else None
            )
        )
        self.select_approver_form = AddApproverForm(
            selected_approver_id=(
                intance_request.approver.id if intance_request.approver else None
            )
        )

        if intance_request.type == "Cuenta de Cobro":
            gotten_request = ChargeAccountRequest.objects.get(pk=request_id)
        if intance_request.type == "Legalización de Factura":
            gotten_request = InvoiceLegalizationRequest.objects.get(pk=request_id)

        return render(
            request,
            self.template_name,
            {
                "request": gotten_request,
                "user": request.user,
                "select_reviewer": self.select_reviewer_form,
                "select_approver": self.select_approver_form,
            },
        )
