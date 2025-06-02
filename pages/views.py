from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from listings.models import Listing  # Import the Listing model to use in views
from realtors.models import Realtor  # Import the Realtor model to use in views
# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World</h1>")   #testing
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]  # Get all listings ordered by list date, only published ones
    context = {"listings": listings}  # Create a context dictionary to pass to the template
    return render(request,'pages/index.html', context) 

def about(request):
    # pages_url = reverse('pages:about')  # get the url of about page
    realtors_base = Realtor.objects.all()
    realtors = realtors_base.order_by('-hire_date')  # Order realtors by hire date
    mvp_realtors = realtors_base.filter(is_mvp=True)  # Filter realtors to get only MVPs
    context = {"realtors": realtors, "mvp_realtors":mvp_realtors}  # Create a context dictionary to pass to the template
    return render(request,'pages/about.html', context)
    # Method 2
    # realtors = Realtor.objects.order_by('-hire_date')  # Order realtors by hire date
    # mvp_realtors = Realtor.objects.filter(is_mvp=True)  # Filter realtors to get only MVPs
    # context = {"realtors": realtors, "mvp_realtors"}  # Create a context dictionary to pass to the template