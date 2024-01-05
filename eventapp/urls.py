from django.urls import path

from eventapp import views

urlpatterns=[
    path("",views.home,name="home"),
    path("index",views.task,name="index"),
    path("teacher", views.teacher_login, name="teacher"),
    path("student", views.student_login, name="student"),
    path("admintemp", views.admintemp, name="admintemp"),
    path("teach", views.teacher, name="teach"),
    path("stu", views.student, name="stu"),
    path("login_view", views.login_view, name="login_view"),
    path("stuview", views. stu_read, name="stuview"),
    path("teachview", views.teach_read, name="teachview"),
    path("studelt/<int:id>/", views.stu_delt, name="studelt"),
    path("teachdelt/<int:id>/", views.teach_delt, name="teachdelt"),
    path("stuupdate/<int:id>/", views.stu_update, name="stuupdate"),
    path("teachupdate/<int:id>/", views.teach_update, name="teachupdate"),
    path("club", views.club, name="club"),
    path("clubview", views.club_view, name="clubview"),
    path("clubdelt/<int:id>/", views.club_delt, name="clubdelt"),
    path("clubupdate/<int:id>/", views.club_update, name="clubupdate"),
    path("viewclub", views.teach_club_view, name="viewclub"),
    path("event/<int:id>/", views.create_event, name="event"),
    path("eventview", views.event_view, name="eventview"),
    path("eventupdate/<int:id>/", views.event_update, name="eventupdate"),
    path("not", views.notification, name="not"),
    path("notview", views.not_view, name="notview"),
    path("stunotview", views.student_not_view, name="stunotview"),
    path("teachnotview", views.teach_not_view, name="teachnotview"),
    path("stufeedback", views.stu_feedback, name="stufeedback"),
    path("viewfeedback", views.feedback_view, name="viewfeedback"),
    path("adminfeedback", views.admin_feedback_view, name="adminfeedback"),

]
