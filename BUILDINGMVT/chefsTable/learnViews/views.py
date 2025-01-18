from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.

# Function based Views - imperative in Nature
def learnHttpMethods(request):
    if request.method=='GET':  
        #perform read or delete operation on the model
        # val = request.GET['key']  
        print(request)
        return HttpResponse("This is a GET request")
    if request.method=='POST':  
        #perform insert or update operation on the model
        # val = request.GET['key']
        return HttpResponse("This is a POST request")
        # context={ } #dict containing data to be sent to the client  

    # return render(request, 'mytemplate.html', context)
    

# Class Based Views
class MyView(View):
    def get(self, request):
        # logic to process get data
        return HttpResponse('response to get Request')
    
    def post(self, request):
        # logic to process get data
        return HttpResponse('response to post Request')
    