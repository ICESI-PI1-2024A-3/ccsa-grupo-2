from django.shortcuts import redirect, render
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
# from ..models import 

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