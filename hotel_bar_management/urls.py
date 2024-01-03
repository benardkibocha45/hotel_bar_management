from django.contrib import admin
from django.urls import path, include
from rooms.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('rooms/', include('rooms.urls')),
    path('bar/', include('bar.urls')),      
    path('users/', include('users.urls')),  
    # Add other top-level URLs as needed
]
