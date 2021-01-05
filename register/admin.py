from django.contrib import admin
from .models import UserProfile
# Register your models here.




class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phonenumber','birth_date', 'site','id',]

admin.site.register(UserProfile, UserProfileAdmin)

