from django.views import View
from django.shortcuts import redirect, HttpResponse
from ..models import *


class DeleteRequestView(View):
    def get(self,request,request_id,*args, **kwargs):
        #request_type = Request.objects.get(pk=request_id).type
        instance_request = Request.objects.get(pk=request_id)
        print('\n\n REQUEST ID : ',request_id)
        instance_request.delete()

        return redirect('requests_list')
    
        




