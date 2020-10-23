from django.http import HttpResponse
from django.http import HttpRequest

def index(request:HttpRequest):
    return HttpResponse(f"Hello world! You are at the polls index. {request.GET['name']}")


def test(request):
    return HttpResponse("Hello world! You are at the polls test.")