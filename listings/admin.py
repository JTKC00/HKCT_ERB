from django.contrib import admin

# Register your models here.
from .models import Listing # Import the Listing model from models.py

admin.site.register(Listing) 
# Register the Listing model with the admin site to manage listings through the Django admin interface