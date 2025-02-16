from django.contrib import admin
from django.urls import path
from APP import views

urlpatterns = [
    # Admin Routes
    path("admin/", views.adminpage, name="adminpage"),

    # Authentication Routes
    path("login_all/", views.login_all, name="login_all"),
    path("logout_all/", views.log_out_function, name="logout_all"),


    # Homepages
    path("", views.homepage, name="homepage"),
    path("studhome/", views.student_home_page, name="studhome"),
    path("teachhome/", views.teacher_home_page, name="teachhome"),

    # Student Management
    path("studreg/", views.student_register, name="student_register"),
    path("edit_student/", views.edit_student, name="edit_student"),
    path("update_student/<int:id>/", views.update_student, name="update_student"),
    path("view_student_admin/", views.view_student_by_admin, name="view_student_admin"),
    path("teachhome/view_student_teacher/", views.view_student_by_teacher, name="view_student_teacher"),
    path("del_student/<int:id>/", views.delete_student_by_admin, name="del_student"),
    path("stud_approve/<int:id>/", views.approve_student_by_admin, name="stud_approve"),

    # Teacher Management
    path("add_teacher/", views.teacher_register, name="add_teacher"),
    path("teachhome/edit_teacher/", views.edit_teacher, name="edit_teacher"),
    path("teachhome/update_teacher/<int:id>/", views.update_teacher, name="update_teacher"),
    path("view_teacher_admin/", views.view_teacher_by_admin, name="view_teacher_admin"),
    path("view_teacher_student/", views.view_teacher_by_student, name="view_teacher_student"),
]