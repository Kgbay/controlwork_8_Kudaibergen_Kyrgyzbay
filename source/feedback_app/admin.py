from django.contrib import admin
from .models import Product, Review


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'description')
    list_filter = ('id', 'name', 'category', 'created_at')
    search_fields = ('name', 'category', 'description')
    fields = ('name', 'category', 'description', 'image')


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'text', 'grade', 'created_at')
    list_filter = ('author', 'product', 'grade', 'created_at')
    search_fields = ('author', 'product', 'grade', 'created_at')
    fields = ('author', 'product', 'text', 'grade')


admin.site.register(Review, ReviewAdmin)
