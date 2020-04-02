from django.shortcuts import render
from .models import Currency

# Create your views here.
def index(request):
    currency = Currency.objects.all()
    context = {'currency':currency}
    return render(request, 'currency/currency_lists.html', context)

