from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse
from .tasks import time_wasted

# Create your views here.


class Enduser(View):

    def get(self, request):
        t = 1
        time_wasted.delay()
        return HttpResponse("done")

    def post(self, request):
        pass
