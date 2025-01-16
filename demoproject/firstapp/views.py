from django.shortcuts import render
# import for HttpResponse
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, World. This is the index view of the firstapp.")

# new content for homepage
def homepage(request):
    return HttpResponse("HomePage")