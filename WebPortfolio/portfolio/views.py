from django.shortcuts import render
from .models import Projeto # Importa o banco de dados

def home(request):
    meus_projetos = Projeto.objects.all().order_by('-criado_em')
    return render(request, 'index.html', {'projetos': meus_projetos})