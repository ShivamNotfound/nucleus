from django.urls import path
from . import views 

urlpatterns=[path('',views.home,name='home'),
             path('Createtask',views.addtask,name='add-task'),
             path('Modify_Task/<int:id>',views.altertask,name='altertask'),
             path('DeleteTask/<int:id>',views.deletetask,name='delete-task'),
             path('login/',views.loginuser,name='login'),
             path('signup/',views.signupuser,name='sign-up'),
             path('logout/',views.logoutuser,name='logout'),
             path("prev_history/<str:date>/",views.prev_hist,name='prev_hist'),
             path("history/<str:date>/",views.succ_hist,name='succ_hist')]