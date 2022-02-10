from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    #return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a> ")
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
    context_dict1 = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake, juice!'}
    #return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html', context = context_dict1)