from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from eventapp.forms import LoginRegister, TeacherForm, StudentForm, ClubForm, EventForm, NotificationForm, FeedbackForm, \
    ReplyForm
from eventapp.models import Student, Teacher, Club, Event, Notification, Feedback, Reply


# Create your views here.
def home(request):
    return render(request,"home.html")
def task(request):
    return render(request,"index.html")

def teacher_login(request):
    Login_form = LoginRegister()
    Teacher_form = TeacherForm()
    if request.method == "POST":
        Login_form = LoginRegister(request.POST)
        Teacher_form = TeacherForm(request.POST)

        if Login_form.is_valid() and Teacher_form.is_valid():
            user2=Login_form.save(commit=False)
            user2.is_teacher=True
            user2.save()
            user1=Teacher_form.save(commit=False)
            user1.user_1=user2
            user1.save()
            return redirect("login_view")
    return render(request,'form.html',{'Login_form':Login_form,'Teacher_form':Teacher_form})



def student_login(request):
    Login_form = LoginRegister()
    Student_form = StudentForm()
    if request.method == "POST":
        Login_form = LoginRegister(request.POST)
        Student_form = StudentForm(request.POST)

        if Login_form.is_valid() and Student_form.is_valid():
            user2=Login_form.save(commit=False)
            user2.is_student=True
            user2.save()
            user1=Student_form.save(commit=False)
            user1.user_2=user2
            user1.save()
            return redirect("login_view")
    return render(request,'student.html',{'Login_form':Login_form,'Student_form':Student_form})

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("admintemp")
            elif user.is_teacher:
                return redirect("teach")
            elif user.is_student:
                return redirect("stu")
        else:
            messages.info(request,'Invalid credentials')
    return render(request,'Login.html')
