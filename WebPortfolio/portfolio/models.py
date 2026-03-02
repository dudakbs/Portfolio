from django.db import models

class Tecnologia(models.Model):
    nome = models.CharField(max_length=50, help_text="Ex: Python, C++, Django, Biomecânica")

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tag = models.CharField(max_length=50)
    data = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to='projetos_capas/', blank=True, null=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name="projetos")
    
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo