from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from eventapp.forms import LoginRegister, TeacherForm, StudentForm, ClubForm, EventForm, NotificationForm, FeedbackForm
from eventapp.models import Student, Teacher, Club, Event, Notification, Feedback


# Create your views here.
def home(request):
    return render(request,"home.html")
def task(request):
    return render(request,"index.html")
def admintemp(request):
        return render(request,"admintemp/base.html")



def teacher(request):
    return render(request,"teacher/base.html")


def student(request):
    return render(request,"student/base.html")

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


def stu_read(request):
    data=Student.objects.all()
    return render(request,"admintemp/studentview.html",{"data":data})

def teach_read(request):
    data=Teacher.objects.all()
    return render(request,"admintemp/teacherview.html",{"data":data})


def stu_delt(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect("stuview")


def stu_update(request,id):
    student=Student.objects.get(id=id)
    form=StudentForm(instance=student)
    if request.method == 'POST':
        form=StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("stuview")
    return render(request,"admintemp/studentupdate.html",{'form':form})

def teach_delt(request,id):
    data=Teacher.objects.get(id=id)
    data.delete()
    return redirect("teachview")


def teach_update(request,id):
    teach=Teacher.objects.get(id=id)
    form=TeacherForm(instance=teach)
    if request.method=='POST':
        form=TeacherForm(request.POST,instance=teach)
        if form.is_valid():
            form.save()
            return redirect("teachview")
    return render(request,"admintemp/teacherupdate.html",{"form":form})


def club(request):
    club=ClubForm()
    if request.method=="POST":
        club=ClubForm(request.POST,request.FILES)
        if club.is_valid():
            club.save()

    return render(request,"admintemp/club.html",{"club":club})


def club_view(request):
    data=Club.objects.all()

    return render(request,"admintemp/clubview.html",{"data":data})


def club_delt(request,id):
    if request.method == "POST":
        data= Club.objects.get(id=id)
        data.delete()
        return redirect("clubview")

def club_update(request,id):
    data=Club.objects.get(id=id)
    form=ClubForm(instance=data)
    if request.method=="POST":
        form=ClubForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect("clubview")
    return render(request,"admintemp/clubupdate.html",{"form":form})

def teach_club_view(request):
    data=Club.objects.all()
    l=request.user.id
    a=Teacher.objects.get(user_1_id=l)
    u=Club.objects.filter(staff_incharge=a)
    print(l)
    print(a.id)
    print(u)

    return render(request,"teacher/viewclub.html",{"data":data,"u":u})


def create_event(request,id):

    data = Club.objects.get(id=id)
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():

            d=form.save(commit=False)
            d.club= data
            d.save()
    return render(request,"teacher/event.html",{"form":form})



def event_view(request):
    data=Event.objects.all()
    r=request.user.id
    t= Teacher.objects.get(user_1_id=r)

    print(r)

    print(t.id)

    data_club = Club.objects.filter(staff_incharge=t)
    print(data_club)
    return render(request,"teacher/eventview.html",{'data_and_club': zip(data,data_club)})



def event_update(request,id):
    data=Event.objects.get(id=id)

    form=EventForm(instance=data)
    if request.method=='POST':
        form=EventForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    return render(request,"teacher/eventupdate.html",{"form":form})


def notification(request):
    form=NotificationForm()
    if request.method == 'POST':
        form=NotificationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"admintemp/notification.html",{"form":form})

def not_view(request):
    data=Notification.objects.all()
    return render(request,"admintemp/notview.html",{"data":data})


def student_not_view(request):
    data=Notification.objects.all()
    return render(request,"student/notview.html",{"data":data})


def teach_not_view(request):
    data=Notification.objects.all()
    return render(request,"teacher/notview.html",{"data":data})


def stu_feedback(request):
    form=FeedbackForm()
    user_1=request.user

    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():

            data=form.save(commit=False)
            data.user=user_1
            data.save()
    return render(request,"student/feedback.html",{'form':form})


def feedback_view(request):
    u=request.user.id
    print(u)

    data=Feedback.objects.filter(user=u)

    return render(request,"student/viewfeedback.html",{'data':data})


def admin_feedback_view(request):
    data=Feedback.objects.all()
    return render(request,"admintemp/feedbackview.html",{'data':data})



