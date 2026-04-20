from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth.models import User

# --- NOTRE SCRIPT SECRET ---
def create_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@admin.com', 'TonMotDePasse123')
        return HttpResponse("<h1>🎉 VICTOIRE ! Superuser créé avec succès !</h1> <p>Tu peux maintenant aller sur /admin/</p>")
    return HttpResponse("<h1>👍 Le superuser existe déjà !</h1> <p>Va te connecter sur /admin/</p>")
# ---------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setup-admin/', create_admin),  # <-- Le lien secret
]