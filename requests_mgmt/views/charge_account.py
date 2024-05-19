from django.conf import settings
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from pathlib import Path
import os

from ..forms import (
    BankInformation,
    CheckboxRentResidentForm,
    CityDateForm,
    NewChargeAccountForm,
    TaxTreatmentForm,
    UserInfoForm,
    UploadDocuments
)
from ..models import ChargeAccountRequest,RequestStatus


class ChargeAccountView(View):
    template_name = "requests/create_charge_account_request.html"
    bank_info_form = BankInformation
    checkbox_form = CheckboxRentResidentForm
    city_date_form = CityDateForm
    charge_account_form = NewChargeAccountForm
    tax_treatment_form = TaxTreatmentForm
    user_info_form = UserInfoForm
    upload_documents = UploadDocuments

    def get(self, request, *args, **kwargs):
        initial_data = {
            "user_name": request.user,
            "user_id": request.user.id_number,
            "document_type": request.user.id_type
        }
        user_info_form = self.user_info_form(initial=initial_data)
        
        return render(
            request,
            self.template_name,
            {
                "bank_info_form": self.bank_info_form(),
                "checkbox_form": self.checkbox_form(),
                "city_date_form": self.city_date_form(),
                "charge_account_form": self.charge_account_form(),
                "tax_treatment_form": self.tax_treatment_form(),
                "user_info_form": user_info_form,
                "upload_documents": self.upload_documents
            },
        )

    def post(self, request, *args, **kwargs):
        try:
            amount = request.POST.get("amount")
            concept = request.POST.get("concept")
            city = request.POST.get("city")
            date = request.POST.get("date")
            bank_name = request.POST.get("bank_name")
            account_type = request.POST.get("account_type")
            account_number = request.POST.get("account_number")
            cex_no = request.POST.get("cex_no")
            rent_tax_declarant = request.POST.get("rent_tax_declarant")
            fiscal_resident = request.POST.get("fiscal_resident")
            costs_and_deductions = request.POST.get("checkbox_choices")
            requester = request.user

            bankCertificate_file_path = ""
            rut_file_path = ""

            rut_document = request.POST.get("documents")
            if rut_document!="":
                form = UploadDocuments(request.POST, request.FILES)
                if form.is_valid():
                    uploaded_file = request.FILES['documents']
                    if uploaded_file.name.endswith('.pdf'):
                        rut_file_path = self.handle_uploaded_file(uploaded_file)
            
            bc_document = request.POST.get("bank_certificate")
            if bc_document!="":
                form = UploadDocuments(request.POST, request.FILES)
                if form.is_valid():
                    uploaded_bc = request.FILES['bank_certificate']
                    if uploaded_bc.name.endswith('.pdf'):
                        bankCertificate_file_path = self.handle_uploaded_file(uploaded_bc)

            chargeRequest = ChargeAccountRequest.objects.create(
                requester=requester,
                type = 'Cuenta de Cobro',
                status = RequestStatus.objects.get(id=1),
                amount=amount,
                concept=concept,
                city=city,
                costs_and_deductions=costs_and_deductions,
                date=date,
                bank_name=bank_name,
                account_type=account_type,
                account_number=account_number,
                cex_no=cex_no,
                rut_file_path = rut_file_path,
                bank_certificate_file_path=bankCertificate_file_path,

            )
            if rent_tax_declarant:
                chargeRequest.isRent_Tax_Declarant(True)
            else:
                chargeRequest.isRent_Tax_Declarant(False)

            if fiscal_resident:
                chargeRequest.isFiscal_Resident(True)
            else:
                chargeRequest.isFiscal_Resident(False)

            chargeRequest.save()

            return redirect("requests_made")
    
        except ValueError as e:
            print(e)
            return HttpResponse("An Error Has Ocurred")
    
    def handle_uploaded_file(self, uploaded_file):
        upload_dir = os.path.join(settings.BASE_DIR, 'archivos')
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        file_path = os.path.join(upload_dir, uploaded_file.name)

        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        return file_path
