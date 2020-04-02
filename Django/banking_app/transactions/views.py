from django.shortcuts import render
from .models import Transactions

# Create your views here.
def index(request):
    transactions = Transactions.objects.all()
    context = {'transaction':transactions}
    return render(request, 'transactions/transaction_lists.html', context)

