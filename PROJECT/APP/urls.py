from django.urls import path
from .views import homepage, teacher_register, student_register, login_all, adminpage, teacher_home, student_home, view_teacher_admin,logout_all,update_student

urlpatterns = [
    path('', homepage),
    path('tr', teacher_register ),  
    path('sr', student_register),  
    path('login/', login_all),  
    path('adminpage', adminpage,), 
    path('teacher_home', teacher_home),  
    path('student_home', student_home),  
    path('vt_a', view_teacher_admin), 
    path('logout_all',logout_all),
    path('update_student',update_student)
    
]
