from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("This is about view")

def login(request):
    return render(request,"login.html")