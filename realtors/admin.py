from django.contrib import admin

from .models import Realtor  # Import the Realtor model from models.py
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')  # Fields to display in the admin list view
    list_display_links = ('id', 'name')  # Fields that are clickable links in the admin list view
    search_fields = ('name',)  # Fields to search in the admin interface
    list_per_page = 25  # Number of realtors per page in the admin list view


admin.site.register(Realtor, RealtorAdmin)  
# Register the Realtor model with the admin site using the RealtorAdmin configuration