from django.urls import path
from .views import homepage, teacher_register, student_register, login_all, adminpage, teacher_home, student_home, view_teacher_admin

urlpatterns = [
    path('', homepage),
    path('tr', teacher_register ),  
    path('sr', student_register),  
    path('login', login_all),  
    path('adminpage', adminpage,), 
    path('t_h', teacher_home),  
    path('s_h', student_home),  
    path('vt_a', view_teacher_admin), 
    path()
]
