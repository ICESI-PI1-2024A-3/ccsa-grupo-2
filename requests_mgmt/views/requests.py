from django.shortcuts import render
from django.views import View


class RequestsView(View):
    template_name = "requests_index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
