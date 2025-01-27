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

def logout_all(request):
    logout(request)
    return redirect(homepage)

def edit_student(request):
     x=request.session.get('student_id')
     y=Student.objects.get(student_id_id=x)
     z=User.objects.get(id=x)
     return render (request,"edit_student.html",{'views':y,'data':z})

def update_student(request,id):
    if request.method=='POST':
      q=User.objects.get(id=id)
      p=Student.objects.get(student_id_id=q)
      q.first_name=request.POST["firstname"]
      q.last_name=request.POST["lastname"]
      q.email=request.POST["email"]
      q.username=request.POST["username"]
      q.password=request.POST["password"]
      print(q)
      q.save()
      p.address=request.POST["address"]
      p.phone_number=request.POST["phonenumber"]
      print(p)
      p.save()
      return redirect(student_home)

def view_teacher_by_student(request):
   v=Teacher.objects.select_related('teacher_id').all()
   return render(request,'view_teacher_student.html',{'view':v})

def edit_teacher(request):
   x=request.session.get('teacher_id')
   y=Teacher.objects.get(teacher_id_id=x)
   z=User.objects.get(id=x)
   return render (request,"edit_teacher.html", {'view':y ,'data':z})

def update_teacher(request,id):
   if request.method=='POST':
      q=User.objects.get(id=id)
      p=Teacher.objects.get(teacher_id_id=q)

      q.first_name=request.POST["firstname"]
      q.last_name=request.POST["lastname"]
      q.email=request.POST["email"]
      q.username=request.POST["username"]
      q.password=request.POST["password"]
      q.save()

      p.address=request.POST["address"]
      p.phone_number=request.POST["phonenumber"]
      p.experience=request.POST["experience"]
      p.salary=request.POST["salary"]

      p.save()
      return redirect(teacher_home)

   

def view_student_by_teacher(request):
   s=Student.objects.select_related('student_id').all()
   return render (request,"view_student_teacher.html",{'view':s})
