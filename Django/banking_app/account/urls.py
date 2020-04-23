from django.conf.urls import url
from . import views

urlpatterns = [
    url('accounts/', views.index, name='index'),
    url('balance/<int:pk>', views.Acc_balance, name='Acc_balance'),
]
