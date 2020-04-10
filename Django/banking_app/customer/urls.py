from django.conf.urls import url
from . import views
from . import models
app_name='customer'


urlpatterns = [
    url('customers/', views.customer_index, name='customer_index'),
    url('customer/add/', views.add_customer, name='add_customer'),
    url('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    
]

