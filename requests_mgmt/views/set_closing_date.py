from django.shortcuts import redirect, render
from django.views import View

from requests_mgmt.models import Request

class SetClosingDate(View):

    def get(self, request,request_id, *args, **kwargs):
        try:
            instance_request = Request.objects.get(pk=request_id)
            date =request.GET.get('closing_date')
            instance_request.closing_date = date
            instance_request.save()
            return redirect('detail_request',request_id=request_id)
        except Exception:
            return redirect('detail_request',request_id=request_id)
        