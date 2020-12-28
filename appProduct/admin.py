from django.contrib import admin
from .models import Category, Product, Gender
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('datecreated',)
    list_display = ['id','user','name','category', 'price', 'quantity','gender','datecreated']
    list_per_page = 15
    search_fields = ('id',)
    
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Gender)
