from django.shortcuts import render 

# Create your views here.
def index(request):
    return render(request,'dashboard/dashboard.html',{})


# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm

# # Create your views here.
# # def loginPage(request):
# #     form = UserCreationForm
# #     context = {'form':form}
# #     return render(request, '/login.html', context)


# def registerPage(request):
#     form = UserCreationForm()
    
#     if request.method=="POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#     context = {'form':form}
#     return render(request, 'dashboard/register.html', context)