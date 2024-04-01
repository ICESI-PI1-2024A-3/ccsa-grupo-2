from django.views import View

from users_mgmt.models import CustomUser
from ..models import Request
from django.shortcuts import redirect

class UpdateApproverView(View):

    def post(self, request,request_id, *args, **kwargs):
        user_id = request.POST.get('Aprovadores')
        intance_request = Request.objects.get(pk=request_id)
        if user_id is None or intance_request is None:
            return redirect('detail_request', request_id=request_id)
        user = CustomUser.objects.get(pk=user_id)
        intance_request.approver = user
        intance_request.save()
        return redirect('detail_request', request_id=request_id)
