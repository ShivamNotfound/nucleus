from django.urls import path
from . import views 

urlpatterns=[path('',views.home,name='home'),
             path('/Createtask',views.addtask,name='add-task')]