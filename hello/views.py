from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! A change to see if git puts it in the right place")
