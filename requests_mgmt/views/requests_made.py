from django.shortcuts import render
from django.views import View

from ..models import Request


class RequestsMadeView(View):
    template_name = "requests_made.html"
    paginate_by = 10

    def get(self, request):
        requests_made = Request.objects.filter(requester=request.user)
        return render(
            request,
            self.template_name,
            {
                "requests": requests_made,
            },
        )
