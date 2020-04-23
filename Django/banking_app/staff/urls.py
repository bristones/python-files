from django.conf.urls import url
from django.urls import path
from . import views
app_name= 'staff'

urlpatterns = [
    # path('staff/', views.index, name='index'),
    path('login/', views.staffLogin, name='s_Login'),
    path('menu',views.menu_section,name='menu_section'),
]
