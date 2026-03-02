from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # Rota do painel de controle (Jazzmin)
    path('admin/', admin.site.urls),
    
    # Rota do seu app principal do portfólio
    path('', include('portfolio.urls')),
]

# Configuração para o Django carregar as imagens de upload no ambiente local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)