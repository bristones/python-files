from django.shortcuts import render,redirect
from account.models import Account
from account.models import Customer
from .models import SendMoney
from .models import Withdrawal
from .models import Deposit


# Create your views here.
def Send_index(request):
    if request.method =="POST":
        form =request.POST
        #print(form)
        sendmoney= SendMoney()
        sendmoney.recipient_name = form['recipient_name']
        sendmoney.mobile = form['mobile']
        sendmoney.amount = form['amount']
        sendmoney.AccNo = Account.objects.get(pk=form['AccNo'])
        sendmoney.save()   #insert in database
        
        #give us a new id of the recorded item (use the appname and the viewnametag)
        # return redirect ('transactions:send_index' )
    return render(request, 'transactions/sendMoney.html', {})

def Withdrawal_index(request):
    if request.method =="POST":
        form =request.POST
        #print(form)
        withdraw = Withdrawal()
        withdraw.amount = form['amount']
        withdraw.AccNo = Account.objects.get(pk=form['AccNo'])
        withdraw.save()   #insert in database
        
        #give us a new id of the recorded item
        # return redirect ('dashboard:dashboard', withdraw)
    return render(request, 'transactions/withdrawMoney.html', {})

def Deposit_index(request):
    if request.method =="POST":
        form =request.POST
        #print(form)
        deposit= Deposit()
        deposit.amount = form['amount']
        deposit.AccNo = Account.objects.get(pk=form['AccNo'])
        deposit.save()   #insert in database
        
        #give us a new id of the recorded item
        # return redirect ('dashboard:dashboard, deposit)
    return render(request, 'transactions/loadMoney.html', {})

def customerProfile(request):
        # context = {
        #        }
        return render(request, "transactions/customer_profile.html")


def CustomerLogin(request):
   
    if request.method == "POST":
        form = request.POST
        mobileN = form['mobile']
        pin = form['pin']
        customer_info = Customer.objects.get(mobile=mobileN)
        if customer_info is not None:
            if customer_info.pin == pin:
                return redirect('transactions:customer_profile')
            else:
                messages.info(request,'Invalid Phone or Pin')
        else:
            messages.info(request,'Invalid Phone or Pin')
            
    context = {}
    return render(request,"transactions/customer_profile.html",context)

