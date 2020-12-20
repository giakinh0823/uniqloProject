from django.contrib import admin
from .models import Category, Product, Order, OrderDetail
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('datecreated',)

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

class OrderDetailAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

    
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)