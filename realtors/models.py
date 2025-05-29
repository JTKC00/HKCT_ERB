from django.db import models
from datetime import datetime
# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=200)  # Name of the realtor
    phone = models.CharField(max_length=200) # Phone number of the realtor
    email = models.EmailField(max_length=50, unique=True, blank=False)  # Email address of the realtor, must be unique, cannot be blank
    description = models.TextField(blank=True)  # Description of the realtor
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # Photo of the realtor
    is_mvp = models.BooleanField(default=False)  # Whether the realtor is a Most Valuable Player (MVP)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)  # Date when the realtor was hired

    def __str__(self):
        return self.name  # String representation of the Realtor model, returns the name of the realtor