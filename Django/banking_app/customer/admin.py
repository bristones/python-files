from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile','id_number', 'balance', 'age')
    search_fields = ('name', 'mobile','id_number', 'balance', 'age')

# allow display on admin page
admin.site.register(Customer, CustomerAdmin)