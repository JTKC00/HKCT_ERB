from django.contrib import admin

# Register your models here.
from .models import Listing # Import the Listing model from models.py
from django.forms import NumberInput  # Import NumberInput for custom form field rendering
from django.db import models  # Import models for database interaction
class ListingAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published', 'price', 'list_date', 'realtor'  # Fields to display in the admin list view
    list_display_links = 'id', 'title'  # Fields that are clickable links in the admin list view
    search_fields = 'title', 'description', 'address', 'price' # Fields to search in the admin interface
    list_filter = 'realtor',  # Filters to apply in the admin interface
    list_per_page = 25  # Number of listings per page in the admin list view
    list_editable = 'price', 'is_published'  # Fields that can be edited directly in the admin list view
    ordering = ['-id'] # Order listings by ID in descending order
    prepopulated_fields = {'title': ('title',)}  
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs= {'size': '10'})}}  # Override the form field for price to use a NumberInput widget with a specific size
    show_facets = admin.ShowFacets.ALWAYS  # Always show facets in the admin interface
admin.site.register(Listing, ListingAdmin)  # Register the Listing model with the admin site using the ListingAdmin configuration