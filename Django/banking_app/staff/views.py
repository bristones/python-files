from django.shortcuts import render, redirect
from .models import Staff

# Create your views here.
def menu_section(request):
    return render(request,'base_1/menu_section.html',{})

def staffLogin(request):
   
    if request.method == "POST":
        form = request.POST
        mobile = form['mobile']
        staff_id = form['staff_id']
        staff_info = Staff.objects.get(mobile=mobile)
        
        if (staff_info.staff_id == staff_id):
            return redirect('staff:menu_section')
        else:
            messages.info(request, 'Invalid credentials')
            
        
        
        # print(customer_info)
        # print(customer_info.mobile)
        # print(customer_info.pin)
        # if staff is not None:
        #     print('staff info is not empty')
        #     if staff.pin == pin:
        #         print('Pin Matched redirect')
        #         return redirect('base/menu_section.html', staff_info.pk)
        #     else:
        #         print('Pin NOT Matched ')
        #         messages.info(request,'Invalid Phone or Pin')
        # else:
        #     print('Customer info is none')
        #     messages.info(request,'Invalid Phone or Pin')

    return render(request,"staff/staffLogin.html")