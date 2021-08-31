from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse

def home(request):
    return render(request, "index.html")


def waitlist(request):
    return render(request, "waiting_list.html")