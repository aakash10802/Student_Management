from django.urls import path
from .views import homepage, teacher_register, student_register, login_all, adminpage, teacher_home, student_home, view_teacher_admin, logout_all, update_student, view_student_by_admin, delete_student_by_admin, view_student_by_teacher, view_teacher_by_student, edit_student, edit_teacher, update_teacher

urlpatterns = [
    path('', homepage),
    path('tr/', teacher_register ),
    path('sr/', student_register),
    path('login/', login_all ),
    path('adminpage/', adminpage, ),
    path('teacher_home/', teacher_home ),
    path('student_home/', student_home ),
    path('vt_a/', view_teacher_admin ),
    path('logout_all/', logout_all ),
    path('update_student/<int:id>/', update_student ),
    path('view_student_admin', view_student_by_admin),
    path('delete_student_by_admin/<int:id>/', delete_student_by_admin),
    path('view_student_by_teacher/', view_student_by_teacher),
    path('view_teacher_by_student/', view_teacher_by_student),
    path('edit_student/', edit_student),
    path('edit_teacher/', edit_teacher),
    path('update_teacher/<int:id>/', update_teacher),
]
