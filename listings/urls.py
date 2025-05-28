from django.urls import path
from . import views

app_name = 'listings'
urlpatterns = [
    path('', views.index, name='listings'), # This is the main listings page
    path('<int:listing_id>', views.listing, name='listing'), # This is the detail page for a specific listing
    path('search', views.search, name='search'),# This is the search page for listings
]