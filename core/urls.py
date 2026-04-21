from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import path
from your_app_name import views  # Import your views here

# --- NOTRE SCRIPT SECRET ---
def create_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@admin.com', 'TonMotDePasse123')
        return HttpResponse("<h1>🎉 VICTOIRE ! Superuser créé avec succès !</h1> <p>Tu peux maintenant aller sur /admin/</p>")
    return HttpResponse("<h1>👍 Le superuser existe déjà !</h1> <p>Va te connecter sur /admin/</p>")
# ---------------------------

# core/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setup-admin/', ...), # whatever you have here
    path('', views.home_view, name='home'), # Add this line for the root URL
]