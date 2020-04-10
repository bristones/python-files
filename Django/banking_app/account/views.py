from django.shortcuts import render
from .models import Account

# Create your views here.
def index(request):
    accounts = Account.objects.all()
    context = {'accounts':accounts}
    return render(request, 'account/account_list.html', context)

def Acc_balance(request):
    balance = Account.objects.filter()
    context = {'balance':balance}
    return render(request, 'account/showBalance.html', context)
    