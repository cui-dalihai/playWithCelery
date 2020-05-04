from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import HttpResponse
from .tasks import flow_info

# Create your views here.


class Flow(View):

    def get(self, request):
        t = 1
        flow_info.delay()
        return HttpResponse("done")

    def post(self, request):
        pass
