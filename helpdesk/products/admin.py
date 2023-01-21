from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_available', 'created', 'updated']
    list_filter = ['title', 'created', 'updated', 'price']
    list_editable = ['is_available']
    prepopulated_fields = {'slug': ('title',)}
