from django.shortcuts import render, redirect,HttpResponse
from .models import  Student,Teacher, User
from django.contrib.auth import authenticate,login,logout

def homepage(request):
    return render (request,"homepage.html")
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
    
def student_register(request):
    if request.method=="POST":
        fn=request.POST["firstname"]
        ln=request.POST["lastname"]
        e=request.POST["email"]
        u=request.POST['username']
        p=request.POST["password"]
        a=request.POST["address"]
        ph=request.POST["phonenumber"]
        x=User.objects.create_user(first_name=fn,last_name=ln,username=u,password=p,email=e,usertype="student",is_active=False,is_staff=False)
        x.save()
        y=Student.objects.create(std_id=x,address=a,ph_num=ph)
        y.save()
        return HttpResponse("Register Successfully") 
    else:
        return render(request,"student_reg.html")


def login_all(request):
    if request.method=="POST":
        u=request.POST["username"]
        p=request.POST["password"]
        user=authenticate(username=u,password=p)
        if user is not None and user.is_staff==1:
            return redirect(adminpage)
        elif user is not None and user.is_active==1:
            login(request,user)
            request.session['teacher_id']=user.id
            return redirect(teacher_home)
        elif user is not None and user.is_active==1:
            login(request,user)
            request.session['student_id']=user.id
            return redirect(student_home)
        else:
            return HttpResponse("Invalid User")
    
    else:
        return render(request,"login.html")
    
def adminpage(request):
    return render(request,"admin.html")

def teacher_home(request):
    return render(request,"staff_profile.html")

def student_home(request):
    return render(request,"std_profile.html")    

def view_teacher_admin(request):
    v=Teacher.objects.select_related('teacher_id').all()
    return render(request,"teacher_view.html",{'data':v})
