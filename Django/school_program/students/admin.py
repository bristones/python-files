from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','registration_number','address','age','school')
    search_fields = ('name','registration_number','address','age','school')

# allow display on admin page
admin.site.register(Student, StudentAdmin)