from django.contrib import admin
from .models import Category, Fine

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'cost', 'payed', 'deadline']
    list_filter = ['payed']
    list_editable = ['cost', 'payed']
    prepopulated_fields = {'slug': ('name', )}