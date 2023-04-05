from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from .forms import StudentRegistrationForm, TeacherRegistrationForm, LoginForm
from .models import User, Student, Teacher, Class


def home(request):
    return render(request, 'home.html')

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('Main:login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_registration.html', {'form': form})

def teacher_registration(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_teacher = True
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('Main:login')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'teacher_registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_student:
                return redirect('Main:studentdashboard')
            elif user.is_teacher:
                return redirect('Main:teacherdashboard')
            else:
                return redirect('Main:login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def student_dashboard(request):
    user = request.user
    student = Student.objects.get(user=user)
    classes = Class.objects.filter(students=student)
    return render(request, 'student_dashboard.html', {'student': student, 'classes': classes})

def teacher_dashboard(request):
    user = request.user
    teacher = Teacher.objects.get(user=user)
    classes = Class.objects.filter(teacher=teacher)
    return render(request, 'teacher_dashboard.html', {'teacher': teacher, 'classes': classes})
