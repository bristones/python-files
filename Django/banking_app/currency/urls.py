from django.conf.urls import url
from . import views



urlpatterns = [
    url('currency/', views.index, name='index'),
]


