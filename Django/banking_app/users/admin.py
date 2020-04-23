from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email','username','first_name','last_name','mobile_number','pin','is_active','is_staff')
    search_fields = ('email','username','mobile_number')
admin.site.register(CustomUser,CustomUserAdmin)