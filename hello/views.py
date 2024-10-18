from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! Test change from codespace")
