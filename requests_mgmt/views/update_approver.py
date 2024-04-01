from django.views import View

from users_mgmt.models import CustomUser
from ..models import Request


class UpdateApproverView(View):
    def put(self, user_id, request_id, *args, **kwargs):
        user = CustomUser.objects.get(pk=user_id)
        intance_request = Request.objects.get(pk=request_id)
        intance_request.approver = user
        intance_request.save()