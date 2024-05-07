import os
from django.conf import settings
from django.shortcuts import redirect, render, HttpResponse
from django.views import View

from ..forms import (
    InvoiceLegalizationForm,
    ExpenseRatioForm,
    BalanceDiscountAutorizationForm,
    BankInformation,
    InvoiceLegalizationObservations,
    UserInfoForm,
    UploadDocuments
)
from ..models import InvoiceLegalizationRequest,RequestStatus

class InvoiceLegalizationView(View):
    template_name = "requests/create_invoice_legalization_request.html"
    user_info = UserInfoForm
    invoice_legalization_form = InvoiceLegalizationForm
    expense_ratio_form = ExpenseRatioForm
    balance_discount_autorization_form = BalanceDiscountAutorizationForm
    bank_information = BankInformation
    observations = InvoiceLegalizationObservations
    upload_documents = UploadDocuments


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "user_info": self.user_info(),
            "invoice_legalization_form": self.invoice_legalization_form(),
            "expense_ratio_form": self.expense_ratio_form(),
            "balance_discount_autorization_form": self.balance_discount_autorization_form,
            "bank_information": self.bank_information,
            "observations": self.observations(),
            "upload_documents": self.upload_documents()
        })
    
    def post(self, request, *args, **kwargs):
        try:
            legalization_date = request.POST.get("legalization_date")
            dependency = request.POST.get("dependency")
            destination_city = request.POST.get("destination_city")
            departure_date = request.POST.get("departure_date")
            reason_trip = request.POST.get("reason_trip")
            discount_authorization = request.POST.get("autorizar_descuento")
            bank_name = request.POST.get("bank_name")
            account_type = request.POST.get("account_type")
            account_number = request.POST.get("account_number")
            requester = request.user
            document_path = ""

            document = request.POST.get("documents")
            if document!="":
                form = UploadDocuments(request.POST, request.FILES)
                if form.is_valid():
                    uploaded_file = request.FILES['documents']
                    document_path = self.handle_uploaded_file(uploaded_file)


            invoice_legalization_request = InvoiceLegalizationRequest.objects.create(
                requester = requester,
                type = 'Legalización de Factura',
                status = RequestStatus.objects.get(id=1),
                legalization_date = legalization_date,
                dependency = dependency,
                destination_city = destination_city,
                departure_date = departure_date,
                reason_trip = reason_trip,
                discount_authorization = discount_authorization,
                bank_name = bank_name,
                account_type = account_type,
                account_number = account_number,
                document_path = document_path

            )

            invoice_legalization_request.save()

            return redirect("requests_made")
        except ValueError:
            return HttpResponse("An Error Has Ocurred")  ## CAMBIAR ESTO POR REDIRECCION:
    
    def handle_uploaded_file(self, uploaded_file):
        upload_dir = os.path.join(settings.BASE_DIR, 'archivos')
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        file_path = os.path.join(upload_dir, uploaded_file.name)

        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        return file_path
