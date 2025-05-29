"""
URL configuration for bcre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings # Import settings to access MEDIA_URL and MEDIA_ROOT
from django.conf.urls.static import static # Import static to serve media files during development

urlpatterns = [
    path('', include('pages.urls', namespace='pages')),
    path('listings/', include('listings.urls', namespace='listings')),
    # namespace is used to avoid name conflicts in urls
    path('admin/', admin.site.urls),
    ] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# The static function is used to serve media files during development
# MEDIA_URL is the URL that will be used to access media files
# MEDIA_ROOT is the directory where media files are stored
# The debug_toolbar_urls() function is used to include the URLs for the Django Debug Toolbar
# This allows the toolbar to be displayed in the admin interface and other views
# The include function is used to include the URLs from the pages and listings apps
# The path function is used to define the URL patterns for the project
