from django.shortcuts import render
from .models import Customer

# Create your views here.
def customer_index(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request, 'customer/customer_lists.html', context)

def customer_detail(request,pk):
    customer = Customer.objects.get(pk=pk)
    account = Account.objects.filter(pk=pk)
    context={'customer': customer, 'account':account}
    return render(request,'customer/detail.html', context)


def add_customer(request):
    if request.method =="POST":
        form =request.POST
        #print(form)
        customer= Customer()
        customer.name = form['name']
        customer.mobile = form['mobile']
        customer.id_number = form['id_number']
        customer.address = form['address']
        customer.age = form['age']
        #customer.address = form['address']
        customer.save()   #insert in database
        
        #give us a new id of the recorded item
        return redirect ('customer:detail', school.pk)
    return render(request, 'customer/add.html', {})


            
