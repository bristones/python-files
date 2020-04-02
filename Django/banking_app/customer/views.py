from django.shortcuts import render
from .models import Customer

# Create your views here.
def index(request):
    customer = Customer.objects.all()
    context = {'customer':customer}
    return render(request, 'customer/customer_lists.html', context)

