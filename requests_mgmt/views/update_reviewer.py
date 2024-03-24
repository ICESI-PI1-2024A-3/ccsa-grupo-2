from django.views import View

from users_mgmt.model import CustomUser
from ..models import Request


class UpdateReviewerView(View):
        def put(self, *args, **kwargs):
            user = CustomUser.objects.get(pk=user_id)
            intance_request=Request.objects.get(pk=request_id)
            intance_request.reviewer = user
            intance_request.save()
