from django.contrib import admin
from django.urls import path, include

# --- ADD THESE TWO NEW IMPORTS ---
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

# --- ADD THIS SECURITY RULE AT THE BOTTOM ---
# This tells Django to serve our image files, but only while we are developing locally
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)