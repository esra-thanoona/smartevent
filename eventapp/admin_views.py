from django.contrib import messages
from django.shortcuts import render, redirect

from eventapp.forms import StudentForm, TeacherForm, ClubForm, NotificationForm
from eventapp.models import Club, Student, Teacher, Notification, Feedback


def admintemp(request):
    return render(request, "admintemp/base.html")


def club_view(request):
    data=Club.objects.all()

    return render(request,"admintemp/clubview.html",{"data":data})

def stu_read(request):
    data=Student.objects.all()
    return render(request,"admintemp/studentview.html",{"data":data})

def teach_read(request):
    data=Teacher.objects.all()
    return render(request,"admintemp/teacherview.html",{"data":data})

def stu_update(request,id):
    student=Student.objects.get(id=id)
    form=StudentForm(instance=student)
    if request.method == 'POST':
        form=StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("stuview")
    return render(request,"admintemp/studentupdate.html",{'form':form})

def stu_delt(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect("stuview")


def teach_update(request,id):
    teach=Teacher.objects.get(id=id)
    form=TeacherForm(instance=teach)
    if request.method=='POST':
        form=TeacherForm(request.POST,instance=teach)
        if form.is_valid():
            form.save()
            return redirect("teachview")
    return render(request,"admintemp/teacherupdate.html",{"form":form})

def teach_delt(request,id):
    data=Teacher.objects.get(id=id)
    data.delete()
    return redirect("teachview")


def club(request):
    club=ClubForm()
    if request.method=="POST":
        club=ClubForm(request.POST,request.FILES)
        if club.is_valid():
            club.save()

    return render(request,"admintemp/club.html",{"club":club})

def club_views(request):
    data=Club.objects.all()

    return render(request,"admintemp/clubview.html",{"data":data})

def club_update(request,id):
    data=Club.objects.get(id=id)
    form=ClubForm(instance=data)
    if request.method=="POST":
        form=ClubForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect("clubview")
    return render(request,"admintemp/clubupdate.html",{"form":form})

def club_delt(request,id):
    if request.method == "POST":
        data= Club.objects.get(id=id)
        data.delete()
        return redirect("clubview")


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

def admin_feedback_view(request):
    data=Feedback.objects.all()

    return render(request,"admintemp/feedbackview.html",{'data':data})

def admin_reply(request,id):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request, 'Reply send for feedback')
        return redirect('adminfeedback')
    return render(request, 'admintemp/reply.html', {'feedback': feedback})
