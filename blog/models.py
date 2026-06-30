from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")
    conteudo = models.TextField(verbose_name="Conteúdo")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-data_criacao']