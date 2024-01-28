from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.
class Login(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
class Teacher(models.Model):
    DEPARTMENT=(
        ('CSE','CSE'),
        ('ECE','ECE'),
        ('EEE','EEE'),
        ('ME','ME')
    )
    user_1=models.ForeignKey(Login,on_delete=models.CASCADE)
    teacher_name=models.CharField(max_length=50)

    email=models.EmailField()
    phone_number=models.CharField(max_length=10)
    department=models.CharField(max_length=50,choices=DEPARTMENT)

    def __str__(self):
        return self.teacher_name


class Student(models.Model):
    DEPARTMENT=(
        ('CSE','CSE'),
        ('ECE','ECE'),
        ('EEE','EEE'),
        ('ME','ME')
    )
    user_2=models.ForeignKey(Login,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=50)
    admission_number=models.IntegerField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=10)
    address=models.TextField(max_length=100)
    department=models.CharField(max_length=50,choices=DEPARTMENT)



class Club(models.Model):
    club_name=models.CharField(max_length=50)
    staff_incharge=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    image=models.FileField(upload_to='images/')

    def __str__(self):
        return self.club_name





class Event(models.Model):
    club=models.ForeignKey(Club,on_delete=models.CASCADE)
    event_name=models.CharField(max_length=50)
    description=models.CharField()
    event_date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()


class Notification(models.Model):
    date=models.DateField()
    description=models.CharField()

class Feedback(models.Model):
    user=models.ForeignKey(Login,on_delete=DO_NOTHING)
    date=models.DateField(auto_now=True)
    feedback=models.TextField()
    reply=models.TextField(blank=True,null=True)

class Reply(models.Model):
    reply=models.TextField(blank=True,null=True)