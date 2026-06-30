from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'data_criacao')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'conteudo')
    list_filter = ('data_criacao', 'autor')
    ordering = ['-data_criacao']