from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile','id_number', 'address', 'age', 'pin')
    search_fields = ('name', 'mobile','id_number', 'address', 'age', 'pin')

# allow display on admin page
admin.site.register(Customer, CustomerAdmin)