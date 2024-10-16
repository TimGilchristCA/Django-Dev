from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! Another change from VS code")
