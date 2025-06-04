from django.db import models # Import necessary Django models
from django.utils import timezone # Import timezone for date handling
from realtors.models import Realtor  # Assuming a Realtor model exists in the realtors app
from datetime import datetime # Import datetime for date handling
from listings.choices import district_choices  # Import choices for filtering listings
# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING) # Assuming Realtor model exists /CASCADE is also an option 
    title = models.CharField(max_length=200) # Title of the listing
    price = models.IntegerField() # Price of the listing
    address = models.CharField(max_length=200) # Full address of the listing
    street = models.CharField(max_length=200) # Street address
    district = models.CharField(max_length=50, choices=district_choices.items()) # District or area of the listing
    description = models.TextField(blank=True) # Description of the listing
    bedrooms = models.IntegerField() # Number of bedrooms
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1) # Number of bathrooms
    clubhouse = models.IntegerField() # Number of clubhouses
    sqrt = models.IntegerField() # Square footage of the property
    estate_size = models.FloatField(default=0.0) # Size of the estate in acres
    is_published = models.BooleanField(default=True) # Whether the listing is published
    list_date = models.DateTimeField(auto_now_add=True) # Date when the listing was created
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/') # Main photo of the listing 
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  # Additional photo of the listing
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) #, URL of photos are saved in the database
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) #, but not the actual photo files
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 

    class Meta:
        ordering = ('-list_date',) # Order listings by list date, newest first
        indexes = [models.Index(fields=['-list_date'])] # Create an index on list_date for faster queries

    def __str__(self):
        return self.title # String representation of the Listing model, returns the title of the listing
# record label = 'listings' # Label for the app, used in migrations and admin interface