from django.urls import path
from django.conf.urls import url
from . import views
app_name='students'




urlpatterns = [
    #url('', views.index, name='index'),
    path('students/', views.index, name='students'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/add/', views.add, name="add")
]


