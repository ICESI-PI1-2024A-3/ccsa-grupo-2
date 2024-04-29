from django.shortcuts import redirect, render
from django.views import View

from requests_mgmt.models.request_status import RequestStatus

from ..forms import AddApproverForm, AddReviewerForm
from ..models import (
    ChargeAccountRequest,
    AdvanceRequest,
    InvoiceLegalizationRequest,
    Request,
    )


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
        if intance_request.type == "Legalizacion de Factura":
            gotten_request = InvoiceLegalizationRequest.objects.get(pk=request_id)
        if intance_request.type == "Anticipos":
            gotten_request = AdvanceRequest.objects.get(pk=request_id)
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
    
    def post(self, request, request_id, *args, **kwargs):
        action = request.POST.get("action")
        comment = request.POST.get("comentario") 

        instance_request = Request.objects.get(pk=request_id)
        
        if action == "Aceptar":
            new_status = RequestStatus.objects.get(status="Aceptado")
            instance_request.status = new_status
        elif action == "Aprobar":
            new_status = RequestStatus.objects.get(status="Aprobado")
            instance_request.status = new_status
        elif action == "Rechazar":
            new_status = RequestStatus.objects.get(status="Rechazado")
            instance_request.status = new_status
            
            
        if comment:
            instance_request.comments = comment
        
        instance_request.save()

        if request.user.role == "Reviewer":
            return redirect("approve_as_reviewer")
        elif request.user.role == "Approver":
            return redirect("approve_as_approver")