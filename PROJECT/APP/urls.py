from django.urls import path
from .views import teacher_register
urlpatterns = [
    path('',teacher_register),
    
]
