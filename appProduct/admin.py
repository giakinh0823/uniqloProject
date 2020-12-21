from django.contrib import admin
from .models import Category, Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('datecreated',)


    
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
