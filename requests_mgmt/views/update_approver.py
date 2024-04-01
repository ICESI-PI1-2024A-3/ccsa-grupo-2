from django.views import View

from users_mgmt.models import CustomUser
from ..models import Request
from django.shortcuts import redirect

class UpdateApproverView(View):

    def post(self, request, request_id, *args, **kwargs):
        user_id = request.POST.get('Aprovadores')
        if user_id is None or user_id == '':
            return redirect('detail_request', request_id=request_id)

        try:
            # Si se ha seleccionado un aprobador válido, actualiza la solicitud.
            instance_request = Request.objects.get(pk=request_id)
            user = CustomUser.objects.get(pk=user_id)
            instance_request.approver = user
            instance_request.save()
            return redirect('detail_request', request_id=request_id)
        except (Request.DoesNotExist, CustomUser.DoesNotExist) as e:
            instance_request = Request.objects.get(pk=request_id)
            instance_request.approver = None
            instance_request.save()
            return redirect('detail_request', request_id=request_id)
