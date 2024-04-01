from django.shortcuts import redirect, render
from django.views import View

from ..forms import (
    BankInformation,
    CheckboxRentResidentForm,
    CityDateForm,
    NewChargeAccountForm,
    TaxTreatmentForm,
    UserInfoForm,
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

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {
                "bank_info_form": self.bank_info_form(),
                "checkbox_form": self.checkbox_form(),
                "city_date_form": self.city_date_form(),
                "charge_account_form": self.charge_account_form(),
                "tax_treatment_form": self.tax_treatment_form(),
                "user_info_form": self.user_info_form(),
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
            requester = request.user
            chargeRequest = ChargeAccountRequest.objects.create(
                requester=requester,
                status = RequestStatus.objects.get(id=1),
                amount=amount,
                concept=concept,
                city=city,
                date=date,
                bank_name=bank_name,
                account_type=account_type,
                account_number=account_number,
                cex_no=cex_no,
                type="Solicitud Cuenta de Cobro"
            )
            if rent_tax_declarant:
                chargeRequest.isRent_Tax_Declarant(True)
            else:
                chargeRequest.isRent_Tax_Declarant(True)

            if fiscal_resident:
                chargeRequest.isFiscal_Resident(True)
            else:
                chargeRequest.isFiscal_Resident(True)

            chargeRequest.save()
            return redirect("requests_list")
        except ValueError:
            return print("An Error Has Ocurred")  ## CAMBIAR ESTO POR REDIRECCION
