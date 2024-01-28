from django.shortcuts import render, redirect

from eventapp.forms import EventForm
from eventapp.models import Club, Teacher, Event, Notification


def teacher(request):
    return render(request,"teacher/base.html")


def teach_club_view(request):
    data=Club.objects.all()
    # l=request.user.id
    # a=Teacher.objects.get(user_1_id=l)
    # u=Club.objects.filter(staff_incharge=a)
    # print(l)
    # print(a.id)
    # print(u)

    return render(request,"teacher/viewclub.html",{"data":data})


def create_event(request,id):

    data = Club.objects.get(id=id)
    form = EventForm()
    print(form)
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            print("okk")

            d=form.save(commit=False)
            d.club= data
            d.save()
    return render(request,"teacher/event.html",{"form":form})

# def event_view(request):
#     data=Event.objects.all()
#     r=request.user.id
#     t= Teacher.objects.get(user_1_id=r)
#
#     print(r)
#
#     print(t.id)
#
#     data_club = Club.objects.filter(staff_incharge=t)
#     print(data_club)
#     return render(request,"teacher/eventview.html",{'data_and_club': zip(data,data_club)})

def event_view(request):
    data = Event.objects.all()
    return render(request, "teacher/eventview1.html", {"data":data})


def event_update(request,id):
    data=Event.objects.get(id=id)

    form=EventForm(instance=data)
    if request.method=='POST':
        form=EventForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("eventview")
    return render(request,"teacher/eventupdate.html",{"form":form})


def teach_not_view(request):
    data=Notification.objects.all()
    return render(request,"teacher/notview.html",{"data":data})

def event_delt(request,id):
    if request.method == "POST":
        data= Event.objects.get(id=id)
        data.delete()
        return redirect("eventview")
