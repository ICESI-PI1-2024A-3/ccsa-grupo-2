from django.shortcuts import redirect, render,HttpResponse
from django.views import View

from ..forms import (
    UserInfoForm,
    AdvanceRequest
)

from ..models import AdvanceRequest as AdvanceRequestModel,RequestStatus

class AdvanceRequest(View):
    template_name = "requests/create_advance_request.html"
    user_info = UserInfoForm
    advance_request_info = AdvanceRequest

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{
            "user_info": self.user_info(),
            "advance_request_info": self.advance_request_info(),
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
            icesi_last_date = request.POST.get("icesi_last_date")
            payment_order_code = request.POST.get("payment_order_code")
            airport_transport = request.POST.get("airport_transport")
            local_transport = request.POST.get("local_transport")
            food_expense = request.POST.get("food_expense")
            alojamiento = request.POST.get("alojamiento")
            other_expenses = request.POST.get("other_expenses")
            advance_total = request.POST.get("advance_total")
            requester = request.user

            advance_request = AdvanceRequestModel.objects.create(
                requester = requester,
                type = 'Anticipos',
                status = RequestStatus.objects.get(id=1),
                request_date=request_date,
                dependency=dependency,
                destination_city=destination_city,
                departure_date=departure_date,
                return_date=return_date,
                reason_trip=reason_trip,
                advance_currency=advance_currency,
                icesi_last_date=icesi_last_date,
                payment_order_code=payment_order_code,
                airport_transport=airport_transport,
                local_transport=local_transport,
                food_expense=food_expense,
                alojamiento=alojamiento,
                other_expenses=other_expenses,
                advance_total=advance_total,
            )

            advance_request.save()

            return redirect("requests_list")
        except ValueError:
            return HttpResponse('Please enter a Valid Value')
