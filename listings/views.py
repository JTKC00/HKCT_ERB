from django.shortcuts import render, get_object_or_404  # Import render and get_object_or_404 for rendering templates and fetching objects
from listings.models import Listing  # Import the Listing model from models.py
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Import Paginator for pagination functionality
from listings.choices import price_choices, bedroom_choices, district_choices  # Import choices for filtering listings
# Create your views here.
def index(request):
    listings = Listing.objects.all() # Fetch all listings from the database
    paginator = Paginator(listings, 3)  # Create a Paginator object for pagination
    page = request.GET.get('page')  # Get the current page number from the request
    paged_listings = paginator.get_page(page)  # Get the listings for the current page
    context = {'listings': paged_listings}  # Prepare context with paged listings
    return render(request, 'listings/listings.html', context)
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)  # Fetch the listing by ID or return 404 if not found
    context = {'listing': listing,}  # Prepare context with the specific listing
    return render(request, 'listings/listing.html', context)
def search(request):
    queryset_list = Listing.objects.order_by('-list_date')  
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains=title)
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list = queryset_list.filter(district__iexact=district)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    if 'price' in request.GET:  
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    context = {'price_choices': price_choices, 
    'bedroom_choices': bedroom_choices, 
    'district_choices': district_choices,
    "listings": queryset_list, "values": request.GET}  # Prepare context with choices for filtering
    return render(request, 'listings/search.html', context)
