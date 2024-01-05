from django import forms
from django.contrib.auth.forms import UserCreationForm

from eventapp.models import Login, Teacher, Student, Club, Event, Notification, Feedback


class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)
    class Meta:
        model=Login
        fields=("username","password1","password2")


class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'
        exclude=("user_1",)


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        exclude=("user_2",)


class ClubForm(forms.ModelForm):
    class Meta:
        model=Club
        fields='__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
class EventForm(forms.ModelForm):
    event_date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = Event
        fields = '__all__'
        # exclude = ('club',)

class NotificationForm(forms.ModelForm):
    date=forms.DateField(widget=DateInput)

    class Meta:
        model=Notification
        fields='__all__'

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'
        exclude=('reply','user',)