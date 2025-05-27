from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World</h1>")   #testing
    pages_url = reverse('pages:index')  # get the url of index page
    return render(request,'pages/index.html')

def about(request):
    pages_url = reverse('pages:about')  # get the url of about page
    return render(request,'pages/about.html')
    