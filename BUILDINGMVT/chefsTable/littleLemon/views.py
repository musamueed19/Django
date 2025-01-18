from django.shortcuts import render
# import HttpResponse
from django.http import HttpResponse

# Create your views here.

# homepage view for '' route
def home(request):
    content = "<html><body><h1>Welcome to little lemon</h1></body></html>"
    return HttpResponse(content)


# "hello" view for app's base url
def hello(request):
    return  HttpResponse("Hello, world!")


# menu by id - view
def menu_by_id(request, menu_id):
    menu = Menu.objects.get(pk=menu_id);
    # return  HttpResponse(f"{menu.menu_item}: Type of {menu.cuisine} cuisine");
    
    # using template "menu_card.html"
    return render(request, 'menu_card.html', {'menu': menu});

# this is the powerful concept - by splitting the Data, Logic, and Display into (M, V, T)
# developers can create large-scale (data-driven) applications.
# The MVT Architecture allows the developers to easily update the database, logical code, and presentation, and styling to create - Dynamic Web Applications.

# While the Number of files present isnide our project folder, may seem intimidating, We will explore these files throughout the tutorial (course) & also MVT concept in greater detail.



def learnHttpMethods(request):
    if request.method=='GET':  
        #perform read or delete operation on the model
        # val = request.GET['key']  
        return HttpResponse("This is a GET request")
    if request.method=='POST':  
        #perform insert or update operation on the model
        # val = request.GET['key']
        return HttpResponse("This is a POST request")
        # context={ } #dict containing data to be sent to the client  

    # return render(request, 'mytemplate.html', context)
    