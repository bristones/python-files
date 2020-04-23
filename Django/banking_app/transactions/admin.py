from django.contrib import admin
# from .models import All_transactions
from .models import T_type


# Register your models here.
# class All_transactionsAdmin(admin.ModelAdmin):
#     list_display = ('time', 'trans_code', 'amount', 'balance', 'customer')
#     search_fields = ( 'balance', 'trans_code')
    

# # allow display on admin page
# admin.site.register(All_transactions, All_transactionsAdmin)


class T_typeAdmin(admin.ModelAdmin):
    list_display = ('tName','tCode')
    search_fields = ('tName','tCode')

# allow display on admin page
admin.site.register(T_type, T_typeAdmin)
