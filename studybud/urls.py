from django.contrib import admin
from django.urls import path, include




# List of URL routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]
