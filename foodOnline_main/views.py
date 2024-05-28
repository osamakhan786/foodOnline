

from django.http import HttpRequest, HttpResponse


def home(request):
    return HttpResponse("hello")