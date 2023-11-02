from django.contrib import admin

# Register your models here.
from products.models import ProductModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'created_at']
    search_fields = ['title', 'price']
    list_filter = ['created_at']
