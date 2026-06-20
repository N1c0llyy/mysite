from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'preco', 'estoque')  
    search_fields = ('name',)  
    list_filter = ('estoque',)  