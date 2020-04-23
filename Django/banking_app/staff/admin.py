from django.contrib import admin
from .models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'staff_id')
    search_fields = ('mobile', 'staff_id')

# allow display on admin page
admin.site.register(Staff, StaffAdmin)