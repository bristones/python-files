from django.shortcuts import render
from .models import Account


# Create your views here.
def index(request):
    accounts = Account.objects.all()
    context = {'accounts':accounts}
    return render(request, 'account/account_list.html', context)

def Acc_balance(request,pk):
    account = Account.objects.get(pk=pk)
    context = {'account':account}
   
    
    return render(request, 'account/showBalance.html', context)

def service_charge(request):
    fee = 0.05 * amount
    return fee


    