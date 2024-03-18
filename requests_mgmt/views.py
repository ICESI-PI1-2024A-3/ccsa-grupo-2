from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.
class RequestViews:
    def createRequest(request):
        if request.method=='GET':
            return render(request,'createChargeAccountRequest.html',{
                'userInfoForm':user_information(),
                'inputForm':CreateNewChargeAccount()
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
                
                chargeRequest.save()
                return redirect('show_requests')
            except:
                return HttpResponse('An Error Has Ocurred')
            
    
    def showRequests(request):
        requests = ChargeAccountRequest.objects.all()
        return render(request,'requestTable.html',{
            'requests':requests
        })
    
    def detail_request(request,request_id):
        chargeRequest = ChargeAccountRequest.objects.get(id=request_id)
        return render(request,'detail_request.html',{
            'chargeRequest':chargeRequest
        })
    
    def edit_request(request,request_id):
        chargeRequest = ChargeAccountRequest.objects.get(id=request_id)
        if request.method=='GET':
            print("\n\n GET !!!!!!!!!\n\n")
            return render(request,'edit_request.html',{
                'chargeRequest':chargeRequest,
                'form':CreateNewChargeAccount
            })
        else:
            chargeRequest.amount=request.POST['amount']
            chargeRequest.concept=request.POST['concept']
            chargeRequest.city=request.POST['city']
            chargeRequest.date=request.POST['date']
            chargeRequest.bank_name=request.POST['bank_name']
            chargeRequest.account_type=request.POST['account_type']
            chargeRequest.account_number=request.POST['account_number']
            chargeRequest.CEX_no=request.POST['CEX_no']
            chargeRequest.save()
            return redirect('show_requests')
        
                
    def delete_request(request,request_id):
        chargeRequest = ChargeAccountRequest.objects.get(id=request_id)
        chargeRequest.delete()
        return redirect('show_requests')


    
  


            

