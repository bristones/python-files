from django.conf.urls import url
from django.urls import path
from . import views
app_name= 'users'

urlpatterns = [
    path('', views.UserLogin, name='login'),
    

]