from django.urls import path
from django.conf.urls import url
from . import views
app_name='subjects'


urlpatterns = [
    #url('', views.index, name='index'),
    path('subjects/', views.index, name='index'),
    path('subjects/<int:subject_id>/', views.subject_index, name= 'detail'),
    path('subjects/add/', views.add, name="add")
]


