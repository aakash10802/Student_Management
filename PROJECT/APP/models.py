from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate,login,logout

class User(AbstractUser):
    usertype=models.CharField(max_length=100)
    
class Student(models.Model):
    std_id = models.ForeignKey(User,on_delete=models.CASCADE)
    address =models.CharField(max_length=255)
    ph_num=models.IntegerField()
    
class Teacher(models.Model):
    teacher_id=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    phone_number=models.IntegerField()
    experience=models.IntegerField()
    salary=models.IntegerField()