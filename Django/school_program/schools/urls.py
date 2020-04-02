from django.urls import path
from . import views
app_name='schools'

urlpatterns = [
    path('schools/', views.schoolIndex, name='schools'),
    path('schools/<int:school_id>/', views.school_detail, name= 'detail'),
    path('schools/add/', views.add, name="add")
]


