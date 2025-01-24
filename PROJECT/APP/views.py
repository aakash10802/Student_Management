from django.shortcuts import render, redirect,HttpResponse
from .models import  Student,Teacher, User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404
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
       return redirect(login_all)
    else:   
        return render(request,"teacher_reg.html")
    
def student_register(request):
    if request.method == "POST":
        fn = request.POST.get("firstname")
        ln = request.POST.get("lastname")
        e = request.POST.get("email")
        u = request.POST.get("username")
        p = request.POST.get("password")
        a = request.POST.get("address")
        ph = request.POST.get("phonenumber")

        if not all([fn, ln, e, u, p, a, ph]):
            return HttpResponse("All fields are required", status=400)

        x = User.objects.create_user(
            first_name=fn,
            last_name=ln,
            username=u,
            password=p,
            email=e,
            usertype="student",
            is_active=False,
            is_staff=False,
        )
        x.save()
        y = Student.objects.create(std_id=x, address=a, ph_num=ph)
        y.save()

        return render(request, "login.html")
    else:
        return render(request, "student_reg.html")

def login_all(request):
    if request.method=="POST":
        u=request.POST["username"]
        p=request.POST["password"]
        user=authenticate(username=u,password=p)
        if user is not None and user.is_superuser==1:
            return redirect(adminpage)
        elif user is not None and user.is_staff==1:
            login(request,user)
            request.session['teacher_id']=user.id
            return redirect(teacher_home)
        elif user is not None and user.is_active==1:
            login(request,user)
            request.session['std_id']=user.id
            return redirect(student_home)
        else:
            return HttpResponse("User not Approved by Admin , Contact Admin for more details")
    
    else:
        return render(request,"login.html")
# Admin Page
def adminpage(request):
    return render(request,"admin.html")

# Student Home Page
def student_home(request):
    if not request.user.is_authenticated:
        return redirect (login_all)
    x=get_object_or_404(Student,std_id=request.user)
    context={
        'firstname': x.std_id.first_name,
        'lastname':x.std_id.last_name,
    }
    return render(request,"std_profile.html",context) 
# Teacher Home Page
def teacher_home(request):
    if not request.user.is_authenticated:
        return redirect(login_all)
    y =get_object_or_404(Teacher,teacher_id=request.user)
    context1 = {
        'firstname': y.teacher_id.first_name,
        'lastname':y.teacher_id.last_name,
    }
    return render(request,"teacher_home.html",context1)
   

def view_teacher_admin(request):
    v=Teacher.objects.select_related('teacher_id').all()
    return render(request,"teacher_view.html",{'data':v})

def view_student_by_admin(request):
    s=Student.objects.select_related('student_id').all()
    return render(request,"student_view.html",{'data':s})
def delete_student_by_admin(request,id):
    x=Student.objects.get(id=id)
    x.delete()
    y=x.std_id.id
    z=User.objects.filter(id=y)
    z.delete()
    return redirect(view_student_by_admin)
