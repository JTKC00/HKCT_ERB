from django.shortcuts import render
from listings.models import Listing  # Import the Listing model from models.py
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Import Paginator for pagination functionality
# Create your views here.
def index(request):
    listings = Listing.objects.all() # Fetch all listings from the database
    paginator = Paginator(listings, 3)  # Create a Paginator object for pagination
    page = request.GET.get('page')  # Get the current page number from the request
    paged_listings = paginator.get_page(page)  # Get the listings for the current page
    context = {'listings': paged_listings}  # Prepare context with paged listings
    return render(request, 'listings/listings.html', context)
def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)  # Fetch the specific listing
    context = {'listing': listing}  # Prepare context with the specific listing
    return render(request, 'listings/listing.html', context)
def search(request):
    return render(request, 'listings/search.html') 
