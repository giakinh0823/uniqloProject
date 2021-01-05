from django.contrib import admin
from .models import Category, Product, Gender, Color, Size, Variants, ImageProduct
# Register your models here.


class VariantsItemInline(admin.TabularInline):
    model = Variants
    readonly_fields =('id',)
    raw_id_fields = ['product']
    

class ImageProductItemInline(admin.TabularInline):
    model = ImageProduct
    readonly_fields =('id',)
    raw_id_fields = ['product']
    
 

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('datecreated',)
    list_display = ['id','user','name','category', 'price', 'quantity','datecreated']
    list_per_page = 15
    search_fields = ('id',)
    inlines = [ImageProductItemInline, VariantsItemInline]
    
class VariantsAdmin(admin.ModelAdmin):
    list_display = ['id','name','product','gender']
    list_per_page = 15
    search_fields = ('id',)
    
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Gender)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ImageProduct)
admin.site.register(Variants, VariantsAdmin)
