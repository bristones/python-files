from django.conf.urls import url
from django.urls import path
from . import views
app_name= 'transactions'

urlpatterns = [
    path('send/<int:pk>', views.Send_index, name='send_index'),
    path('withdraw/<int:pk>', views.withdrawal_index, name='withdrawal_index'),
    path('do_deposit/<int:pk>', views.Deposit_index, name='deposit_index'),
    path('#',views.CustomerLogin,name='customerlogin'),
    path('profile/<int:pk>',views.customerProfile,name='customer_profile'),
    path('w_report/<int:pk>', views.wReport, name='wReport'),
    path('s_report/<int:pk>', views.sReport, name='sReport'),
    path('d_report/<int:pk>', views.dReport, name='dReport'),
    

]