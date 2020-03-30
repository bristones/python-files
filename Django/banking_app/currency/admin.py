from django.contrib import admin
from .models import Currency

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('CurrName','CurrCode')
    search_fields = ('CurrName','CurrCode')

# allow display on admin page
admin.site.register(Currency, CurrencyAdmin)
