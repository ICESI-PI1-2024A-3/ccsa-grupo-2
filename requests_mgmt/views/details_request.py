from django.shortcuts import redirect, render
from django.views import View
from django.conf import settings
from django.core.mail import EmailMessage
from requests_mgmt.models.request_status import RequestStatus
from ..forms import AddApproverForm, AddReviewerForm
from users_mgmt.models import CustomUser
from ..models import (
    ChargeAccountRequest,
    AdvanceRequest,
    InvoiceLegalizationRequest,
    Request,
    Expense
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

        expenses = []
        if intance_request.type == "Cuenta de Cobro":
            gotten_request = ChargeAccountRequest.objects.get(pk=request_id)
        if intance_request.type == "Legalización de Factura" or intance_request.type == "Legalizacion de Factura":
            gotten_request = InvoiceLegalizationRequest.objects.get(pk=request_id)
            expenses = Expense.objects.filter(request_id_number_id=request_id)
        if intance_request.type == "Anticipos":
            gotten_request = AdvanceRequest.objects.get(pk=request_id)
        if intance_request.type == "":
            gotten_request = AdvanceRequest.objects.get(pk=request_id)
        return render(
            request,
            self.template_name,
            {
                "request": gotten_request,
                "user": request.user,
                "select_reviewer": self.select_reviewer_form,
                "select_approver": self.select_approver_form,
                "expenses":expenses
            },
        )
    
    def post(self, request, request_id, *args, **kwargs):
        action = request.POST.get("action")
        comment = request.POST.get("comentario") 

        instance_request = Request.objects.get(pk=request_id)
        
        if action == "Aceptar":
            new_status = RequestStatus.objects.get(status="Aceptado")
            instance_request.status = new_status
            instance_request.save()  # Cambiar el estado de la solicitud a "Aceptado"

        elif action == "Aprobar":
            new_status = RequestStatus.objects.get(status="Aprobado")
            instance_request.status = new_status
            instance_request.save()
            CustomUser.objects.get
            subject = 'Cambio de estado de solicitud'
            recipient_list = user.email
            template = f"Su solicitud ha finalizado por el proceso de revision y aprovación {user}."
            email = EmailMessage(
                subject,
                template,
                settings.EMAIL_HOST_USER,
                [recipient_list]
                
            )
            email.fail_silently=False
            email.send()
        elif action == "Rechazar":
            new_status = RequestStatus.objects.get(status="Rechazado")
            instance_request.status = new_status
            instance_request.save()
        
        if comment:
            instance_request.comments = comment
        
        instance_request.save()

        if request.user.role == "Reviewer":
            return redirect("approve_as_reviewer")
        elif request.user.role == "Approver":
            return redirect("approve_as_approver")
            