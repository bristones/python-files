from django.conf.urls import url
from . import views
app_name= 'transactions'

urlpatterns = [
    url('send/', views.Send_index, name='send_index'),
    url('withdraw/', views.Withdrawal_index, name='withdrawal_index'),
    url('deposit/', views.Deposit_index, name='deposit_index'),
    url('',views.CustomerLogin,name='customerlogin'),
    url('profile/',views.customerProfile,name='customer_profile'),
    #path('login/',views.logIn,name='login'),
    #path('register/',views.Register,name='register'),
    #path('logout/',views.Logout,name='logout')
]


