from django.urls import path
from . import views

app_name='schools'

urlpatterns = [
    path('schools/', views.schoolIndex, name='school_index'),
    path('schools/<int:pk>/', views.school_detail, name='school_detail'),
    path('schools/add/', views.add, name="add")
    
]
