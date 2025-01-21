from django.shortcuts import render, redirect,HttpResponse
from .models import  Teacher, User

def teacher_register(request):
    if request.method=="POST":
       fn=request.POST["firstname"]
       ln=request.POST["lastname"]
       e=request.POST["email"]
       u=request.POST['username']
       p=request.POST["password"]
       a=request.POST["address"]
       ph=request.POST["phonenumber"]
       ex=request.POST["experience"]
       sa=request.POST["salary"]
       x=User.objects.create_user(first_name=fn,last_name=ln,username=u,password=p,email=e,usertype="teacher",is_active=True,is_staff=True)
       x.save()
       y=Teacher.objects.create(teacher_id=x,address=a,phone_number=ph,experience=ex,salary=sa)
       y.save()
       return HttpResponse("Register Successfully")
    else:   
        return render(request,"teacher_reg.html")