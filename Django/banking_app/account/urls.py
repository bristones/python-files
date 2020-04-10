from django.conf.urls import url
from . import views

urlpatterns = [
    url('index', views.index, name='index'),
    url('balance', views.Acc_balance, name='Acc_balance'),
]
