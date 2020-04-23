from django.conf.urls import url
from . import views


urlpatterns = [
    url('dashboard/', views.index, name='index'),
]
