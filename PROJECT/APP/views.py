from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher, User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Homepage View
def homepage(request):
    return render(request, "homepage.html")

# Student Registration
def student_register(request):
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        un = request.POST['username']
        p = request.POST['password']
        ad = request.POST['address']
        phn = request.POST['phonenumber']

        # Create a User object
        user = User.objects.create_user(
            first_name=fn, last_name=ln, email=em, username=un, password=p, is_active=False
        )

        # Create a Student object with the correct field names
        Student.objects.create(std_id=user, address=ad, ph_num=phn)
        return redirect("login")

    return render(request, "student_reg.html")

# Teacher Registration
def teacher_register(request):
    if request.method == "POST":
        fn = request.POST["firstname"]
        ln = request.POST["lastname"]
        e = request.POST["email"]
        u = request.POST['username']
        p = request.POST["password"]
        a = request.POST["address"]
        ph = request.POST["phonenumber"]
        ex = request.POST["experience"]
        sa = request.POST["salary"]

        # Create a User object
        user = User.objects.create_user(
            first_name=fn, last_name=ln, email=e, username=u, password=p, is_staff=True, is_active=True
        )

        # Create a Teacher object
        Teacher.objects.create(teacher_id=user, address=a, phone_number=ph, experience=ex, salary=sa)
        return redirect("login_all")

    return render(request, "teacher_reg.html")

# Login View
def login_all(request):
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["password"]
        user = authenticate(username=u, password=p)
        if user is not None and user.is_superuser:
            return redirect("adminpage")
        elif user is not None and user.is_staff:
            login(request, user)
            request.session['teacher_id'] = user.id
            return redirect("teachhome")
        elif user is not None and user.is_active:
            login(request, user)
            request.session['std_id'] = user.id
            return redirect("studhome")
        else:
            return HttpResponse("User not Approved by Admin, Contact Admin for more details")
    else:
        return render(request, "login.html")

# Logout View
def log_out_function(request):
    logout(request)
    return redirect("homepage")

# Admin Page
def adminpage(request):
    return render(request, "admin.html")

# Student Home Page
def student_home_page(request):
    if not request.user.is_authenticated:
        return redirect("login")

    student = get_object_or_404(Student, std_id=request.user)
    context = {'firstname': student.std_id.first_name, 'lastname': student.std_id.last_name}
    return render(request, "student_home.html", context)

# Teacher Home Page
def teacher_home_page(request):
    if not request.user.is_authenticated:
        return redirect("login")

    teacher = get_object_or_404(Teacher, teacher_id=request.user)
    context = {'firstname': teacher.teacher_id.first_name, 'lastname': teacher.teacher_id.last_name}
    return render(request, "teacher_home.html", context)

# View Teachers by Admin
def view_teacher_by_admin(request):
    teachers = Teacher.objects.select_related('teacher_id').all()
    return render(request, 'view_teacher.html', {'view': teachers})

# View Students by Admin
def view_student_by_admin(request):
    students = Student.objects.select_related('std_id').all()
    return render(request, "view_student.html", {'view': students})

# Delete Student by Admin
def delete_student_by_admin(request, id):
    student = get_object_or_404(Student, id=id)
    user_id = student.std_id.id
    student.delete()
    User.objects.filter(id=user_id).delete()
    return redirect("view_student_admin")

# Approve Student by Admin
def approve_student_by_admin(request, id):
    student = get_object_or_404(Student.objects.select_related('std_id'), id=id)
    student.std_id.is_active = True
    student.std_id.save()
    return redirect("view_student_admin")

# Edit Student
def edit_student(request):
    student_id = request.session.get('std_id')
    student = get_object_or_404(Student, std_id_id=student_id)
    user = get_object_or_404(User, id=student_id)
    return render(request, "edit_student.html", {'views': student, 'data': user})

# Update Student
def update_student(request, id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=id)
        student = get_object_or_404(Student, std_id=user)

        user.first_name = request.POST["firstname"]
        user.last_name = request.POST["lastname"]
        user.email = request.POST["email"]
        user.username = request.POST["username"]

        if request.POST["password"]:
            user.set_password(request.POST["password"])

        user.save()

        student.address = request.POST["address"]
        student.ph_num = request.POST["phonenumber"]
        student.save()

        return redirect("studhome")

# View Teachers by Student
def view_teacher_by_student(request):
    teachers = Teacher.objects.select_related('teacher_id').all()
    return render(request, 'view_teacher_student.html', {'view': teachers})

# Edit Teacher
def edit_teacher(request):
    teacher_id = request.session.get('teacher_id')
    teacher = get_object_or_404(Teacher, teacher_id_id=teacher_id)
    user = get_object_or_404(User, id=teacher_id)
    return render(request, "edit_teacher.html", {'view': teacher, 'data': user})

# Update Teacher
def update_teacher(request, id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=id)
        teacher = get_object_or_404(Teacher, teacher_id=user)

        user.first_name = request.POST["firstname"]
        user.last_name = request.POST["lastname"]
        user.email = request.POST["email"]
        user.username = request.POST["username"]

        if request.POST["password"]:
            user.set_password(request.POST["password"])

        user.save()

        teacher.address = request.POST["address"]
        teacher.phone_number = request.POST["phonenumber"]
        teacher.experience = request.POST["experience"]
        teacher.salary = request.POST["salary"]
        teacher.save()

        return redirect("teachhome")

# View Students by Teacher
def view_student_by_teacher(request):
    students = Student.objects.select_related('std_id').all()
    return render(request, "view_student_teacher.html", {'view': students})