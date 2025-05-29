from django.contrib import admin

from .models import Realtor  # Import the Realtor model from models.py
# Register your models here.
admin.site.register(Realtor)  # Register the Realtor model with the admin site to manage realtors through the Django admin interface