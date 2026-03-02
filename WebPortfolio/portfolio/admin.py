from django.contrib import admin
from .models import Projeto, Tecnologia 

admin.site.register(Tecnologia)

class ProjetoAdmin(admin.ModelAdmin):
    filter_horizontal = ('tecnologias',)

admin.site.register(Projeto, ProjetoAdmin)
