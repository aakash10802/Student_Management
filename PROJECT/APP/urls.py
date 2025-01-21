from django.urls import path
from .views import teacher_register,student_register
urlpatterns = [
    path('',teacher_register),
    path('st/', student_register),
    
]
