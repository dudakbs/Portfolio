from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static 
from django.views.static import serve        

urlpatterns = [
    # Rota do painel de controle (Jazzmin)
    path('admin/', admin.site.urls),
    
    # Rota do seu app principal do portfólio
    path('', include('portfolio.urls')),
]

# ESTA É A PARTE QUE FORÇA A IMAGEM NA RENDER
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

# Mantendo o padrão por segurança
if settings.DEBUG or not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
