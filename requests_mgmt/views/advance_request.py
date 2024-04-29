from django.shortcuts import redirect, render, HttpResponse
from django.views import View

from ..forms import AdvanceRequest, ExpenseBudget, UploadDocuments, UserInfoForm

from ..models import AdvanceRequest as AdvanceRequestModel,RequestStatus

class AdvanceRequestView(View):
    template_name = "requests/create_advance_request.html"
    user_info = UserInfoForm
    advance_request_info = AdvanceRequest
    expense_budget = ExpenseBudget
    upload_documents = UploadDocuments

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name,{
            "user_info": self.user_info(),
            "advance_request_info": self.advance_request_info(),
            "expense_budget": self.expense_budget(),
            "upload_documents": self.upload_documents()
        })
    
    def post(self, request, *args, **kwargs):
        try:
            request_date = request.POST.get("request_date")
            dependency = request.POST.get("dependency")
            destination_city = request.POST.get("destination_city")
            departure_date = request.POST.get("departure_date")
            return_date = request.POST.get("return_date")
            reason_trip = request.POST.get("reason_trip")
            advance_currency = request.POST.get("advance_currency")
            icesi_last_day_date = request.POST.get("icesi_last_day_date")
            airport_transport = int(request.POST.get("airport_transport"))
            local_transport = int(request.POST.get("local_transport"))
            feeding = int(request.POST.get("feeding"))
            accommodation = int(request.POST.get("accommodation"))
            departure_taxes = int(request.POST.get("departure_taxes"))
            others = int(request.POST.get("others"))
            widget =airport_transport+local_transport+feeding+accommodation+departure_taxes+others
            requester = request.user

            advance_request = AdvanceRequestModel.objects.create(
                requester = requester,
                type = 'Anticipos',
                status = RequestStatus.objects.get(id=1),
                dependency=dependency,
                destination_city=destination_city,
                departure_date=departure_date,
                return_date=return_date,
                reason_trip=reason_trip,
                advance_currency=advance_currency,
                icesi_last_day_date=icesi_last_day_date,
                airport_transport=airport_transport,
                local_transport=local_transport,
                feeding=feeding,
                accommodation=accommodation,
                departure_taxes = departure_taxes,
                others=others,
                widget=widget,
            )

            advance_request.save()

            return redirect("requests_list")
        except ValueError:
            return HttpResponse('Please enter a Valid Value')

