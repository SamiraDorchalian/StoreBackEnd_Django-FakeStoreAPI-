from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'price', 'category', 'rating_rate', 'rating_count')
    search_fields = ('title', 'category')
