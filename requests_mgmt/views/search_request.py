from django.shortcuts import redirect, render
from django.views import View

from requests_mgmt.models import Request

class SearchRequestView(View):
    template_name = "requests/requests_list.html"

    def get(self, request, *args, **kwargs):
        search_query = request.GET.get("search_query")
        print('\n\nSearch Query :',search_query)


        requests = Request.objects.all()
        return render(request, self.template_name, {
            'requests':requests
        })