from django.contrib import admin
from .models import SendMoney


# Register your models here.
class SendMoneyAdmin(admin.ModelAdmin):
    list_display = ('recipient_name', 'mobile','amount')
    search_fields = ('recipient_name', 'mobile','amount')

# allow display on admin page
admin.site.register(SendMoney, SendMoneyAdmin)