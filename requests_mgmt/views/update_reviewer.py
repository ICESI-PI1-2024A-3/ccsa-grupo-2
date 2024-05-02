from django.shortcuts import redirect
from django.views import View
from ..models import Request, RequestStatus
from users_mgmt.models import CustomUser

class UpdateReviewerView(View):

    def post(self, request, request_id, *args, **kwargs):
        user_id = request.POST.get("reviewers")
        if user_id is None or user_id == "":
            return redirect("detail_request", request_id=request_id)

        try:
            instance_request = Request.objects.get(pk=request_id)
            user = CustomUser.objects.get(pk=user_id)
            instance_request.reviewer = user
            instance_request.save()
            
            # Actualizar el estado de la solicitud a "Revisión"
            new_status = RequestStatus.objects.get(status='Revisión')
            instance_request.status = new_status
            instance_request.save()
            
            return redirect("detail_request", request_id=request_id)
        except (Request.DoesNotExist, CustomUser.DoesNotExist) as e:
            instance_request = Request.objects.get(pk=request_id)
            instance_request.reviewer = None
            instance_request.save()
            return redirect("detail_request", request_id=request_id)
