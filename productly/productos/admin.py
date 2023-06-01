from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class ProductAdmin(admin.ModelAdmin):
    exclude = ('creado_en', )
    list_display = ('id', 'nombre', 'stick', 'creado_en')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
