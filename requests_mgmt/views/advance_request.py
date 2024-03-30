from django.shortcuts import redirect, render
from django.views import View

# from ..forms import (
# )

# from ..models import 

class AdvanceRequest(View):
    template_name = "requests/create_advance_request.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,)