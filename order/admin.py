from django.contrib import admin
from .models import Order, OrderDetail, Cart
from django.db.models import Sum, F, FloatField



# Register your models here.

#hướng dẫn
# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     raw_id_fields = ['product']

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id','name', 'mobile_no','address','status', 'created']
#     list_editable = ['status']
#     list_per_page = 15
#     list_filter = ['status']
#     search_fields = ('id',)
#     inlines = [OrderItemInline]



class OrderItemInline(admin.TabularInline):
    model = OrderDetail
    readonly_fields =('id',)
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date', 'get_total_cost')
    list_display = ['id','user','code', 'state', 'quantity','date']
    readonly_fields =('id',)
    list_editable = ['state']
    list_per_page = 15
    list_filter = ['state']
    search_fields = ('id',)
    inlines = [OrderItemInline]



class OrderDetailAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    readonly_fields =('id',)
    list_display = ['id','product','gender', 'quantity', 'totalprice','date']
    list_per_page = 15
    search_fields = ('id',)
    


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Cart)