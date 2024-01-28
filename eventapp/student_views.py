from django.shortcuts import render

from eventapp.forms import FeedbackForm
from eventapp.models import Notification, Feedback, Event


def student(request):
    return render(request,"student/base.html")

def student_not_view(request):
    data=Notification.objects.all()
    return render(request,"student/notview.html",{"data":data})

def stu_event_view(request):
  data=Event.objects.all()
  return render(request,"student/eventview.html",{"data":data})



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

