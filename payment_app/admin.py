from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'desc', 'price', 'thumbnail']


admin.site.register(Product, ProductAdmin)