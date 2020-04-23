from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from account.models import Account
from account.models import Customer
from .models import SendMoney
from .models import Withdrawal
from .models import Deposit
# from .models import All_transactions
from .models import T_type


# Create your views here.
def Send_index(request, pk):
    account = Account.objects.get(pk=pk)
    current_balance = account.balance 
    
    if request.method =="POST":
        form = request.POST
        send = SendMoney()
        send.mobile = float(form['mobile'])
        send.amount = float(form['amount'])
        send.AccNo = float(form['AccNo'])
        if current_balance < withdrawal.amount:
            messages.info(request,'Request failed! your balance of {} is not suficient to complete this transaction'.format(current_balance))
            
        else:
            print(send.amount,send.AccNo) 
            new_balance = current_balance - send.amount
            account.balance = new_balance
            account.save()
            send.save()
            
            messages.success(request,'Confirmed! Ksh {} was sent to {} your new balance is {}'.format(send.amount, send.AccNo, new_balance))

        
    customer = Customer.objects.get(pk=pk)
    context ={
        'customer':customer
    }
    
    return render(request, 'transactions/sendMoney.html', context)


        
def withdrawal_index(request,pk):
    account = Account.objects.get(pk=pk)
    current_balance = account.balance 
    
    if request.method =="POST":
        form = request.POST
        withdrawal = Withdrawal()
        withdrawal.amount = float(form['amount'])
        if current_balance < withdrawal.amount:
            messages.info(request,'Transaction failed! You cannot withdraw an amount that is greater than your balance of {}'.format(current_balance))
            
        else:
            print(withdrawal.amount,withdrawal.AccNo) 
            new_balance = current_balance - withdrawal.amount
            account.balance = new_balance
            account.save()
            withdrawal.save()
            
            messages.success(request,'Transaction sucessful. you made awithdrawal of {}. your new balance is {}'.format(withdrawal.amount, new_balance))

        
    customer = Customer.objects.get(pk=pk)
    context ={
        'customer':customer
    }
    return render(request, 'transactions/withdraw.html',context)

   
def Deposit_index(request,pk):
   
    account = Account.objects.get(pk=pk)
    current_balance = account.balance 
    
    if request.method =="POST":
        form = request.POST
        deposit = Deposit()
        deposit.amount = float(form['amount'])
        
        new_balance = current_balance + deposit.amount
        account.balance = new_balance
        account.save()
        deposit.save()
        
        messages.success(request,'Transaction sucessful. You have made a deposit of {}. your new balance is {}'.format(deposit.amount, new_balance))
        
        customer = Customer.objects.get(pk=pk)
        return redirect('transactions:deposit_index',customer.pk)
    
    customer = Customer.objects.get(pk=pk)
    context ={
        'customer':customer
    }
    return render(request, 'transactions/loadMoney.html',context)
        
        

def customerProfile(request,pk):
    customer = Customer.objects.get(pk=pk)
    account = Account.objects.get(pk=pk)
    context = {
            'customer': customer,
            'account':account
    }
    return render(request, "transactions/customer_profile.html",context)


def CustomerLogin(request):
   
    if request.method == "POST":
        form = request.POST
        mobileN = form['mobile']
        pin = form['pin']
        print(mobileN)
        print(pin)
        customer_info = Customer.objects.get(mobile=mobileN)
        print(customer_info)
        print(customer_info.mobile)
        print(customer_info.pin)
        if customer_info is not None:
            print('Customer info is not empty')
            if customer_info.pin == pin:
                print('Pin Matched redirect')
                return redirect('transactions:customer_profile',customer_info.pk)
            else:
                print('Pin NOT Matched ')
                messages.info(request,'Invalid Phone or Pin')
        else:
            print('Customer info is none')
            messages.info(request,'Invalid Phone or Pin')
            
    context = {}
    return render(request,"transactions/customer_login.html",context)

def wReport(request, pk): 

    customer = Customer.objects.get(pk=pk)
    account = Account.objects.get(pk=pk)
    withdrawals = Withdrawal.objects.filter(pk=pk)
     
    context ={
        'withdrawals':withdrawals,
        'account':account,
        'customer':customer,
    }
    return render(request, "transactions/withdrawReport.html",context)
    
def sReport(request, pk):
    
    customer = Customer.objects.get(pk=pk)
    account = Account.objects.get(pk=pk)
    debit = SendMoney.objects.filter(pk=pk)

    context ={
        'debit':SendMoney,
        'account':account,
        'customer':customer,
    }    
    return render(request, "transactions/sReport.html", context)


def dReport(request, pk):
    customer = Customer.objects.get(pk=pk)
    account = Account.objects.get(pk=pk)
    credit = Deposit.objects.filter(pk=pk)


    context ={
        'credit':Deposit,
        'account':account,
        'customer':customer,
    }      
    return render(request, "transactions/dReport.html", context)
