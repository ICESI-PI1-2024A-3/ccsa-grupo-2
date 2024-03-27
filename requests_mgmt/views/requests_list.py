from django.shortcuts import render
from django.views import View


class RequestsListView(View):
    template_name = "requests_list.html"

    def get(self, request):
        return render(request, self.template_name)
