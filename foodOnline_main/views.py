

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')