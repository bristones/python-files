from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('AccNo', 'AccType', 'balance','currency_id', 'customer_id')
    search_fields = ('AccNo', 'AccType', 'balance','currency_id', 'customer_id')

# allow display on admin page
admin.site.register(Account, AccountAdmin)
