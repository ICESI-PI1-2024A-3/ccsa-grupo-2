from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.
class RequestViews:
    def request_index(request):
        return render(request, 'requests_index.html')


    def charge_account(request):
        if request.method=='GET':
            return render(request,'request_type/charge_account.html',{
                "user_form": user_information(),
                "charge_account": CreateNewChargeAccount(),
                "taxTreatment": TaxTreatmentForm,
                "checkBox": CheckboxRentaResidente,
                "city_date": City_Date,
                "bankInformation": BankInformation
            })
        else:
            try:
                chargeRequest = ChargeAccountRequest.objects.create(
                user_name = request.POST['user_name'],
                user_id=request.POST['user_id'],
                document_type=request.POST['document_type'],
                amount=request.POST['amount'],
                concept=request.POST['concept'],
                city=request.POST['city'],
                date=request.POST['date'],
                bank_name=request.POST['bank_name'],
                account_type=request.POST['account_type'],
                account_number=request.POST['account_number'],
                CEX_no=request.POST['CEX_no']
            )
                costs_and_deductions = request.POST.get('costs_and_deductions',False)
                rent_tax_declarant = request.POST.get('rent_tax_declarant',False)
                fiscal_resident = request.POST.get('fiscal_resident',False)

                if costs_and_deductions:
                    chargeRequest.isCost_and_Deductions(True)
                else:
                    chargeRequest.isCost_and_Deductions(True)
                
                if rent_tax_declarant:
                    chargeRequest.isRent_Tax_Declarant(True)
                else:
                    chargeRequest.isRent_Tax_Declarant(True)
                
                if fiscal_resident:
                    chargeRequest.isFiscal_Resident(True)
                else:
                    chargeRequest.isFiscal_Resident(True)
                return redirect('home')
            except:
                return HttpResponse('An Error Has Ocurred')
            

