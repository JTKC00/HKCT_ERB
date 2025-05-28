from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'listings/listings.html')
def listing(request, listing_id):
    return render(request, 'listings/listing.html') 
def search(request):
    return render(request, 'listings/search.html') 

# The above code defines three views for the listings app:
# 1. `index`: Renders the main listings page.
# 2. `listing`: Renders the detail page for a specific listing, identified by `listing_id`. 
# 3. `search`: Renders the search page for listings.
# These views use Django's `render` function to return the appropriate HTML templates.