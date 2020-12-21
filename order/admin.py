from django.contrib import admin
from .models import Order, OrderDetail, Cart
# Register your models here.



class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

class OrderDetailAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Cart)