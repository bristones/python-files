from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def UserLogin(request):
   
    if request.method == "POST":
        form = request.POST
        username = form['username']
        password  = form['password']
      
        user = authenticate(username=username,password=password)
     
        if user is not None:
            login(request, user)
            customer = Customer.objects.get(user=user)
            context ={'customer':customer}
            return redirect(request, 'transactions:customer_profile', context)
        else:
            messages.info(request,'Invalid username or Password')
            
    return render(request,"users/login.html")


