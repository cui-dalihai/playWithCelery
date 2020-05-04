from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse
from .tasks import issue_create, priorities

# Create your views here.


class Issue(View):

    def get(self, request):
        t = 1
        # issue_create.delay()
        issue_create.apply_async()
        return HttpResponse("done")

    def post(self, request):
        pass


class Priority(View):

    def get(self, request):
        t = 1
        # priorities.delay()
        priorities.apply_async()
        return HttpResponse("done")

    def post(self, request):
        pass


