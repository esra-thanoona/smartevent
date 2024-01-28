from django.urls import path

from eventapp import views, admin_views, teacher_views, student_views

urlpatterns=[
    path("",views.home,name="home"),
    path("index",views.task,name="index"),
    path("teacher", views.teacher_login, name="teacher"),
    path("student", views.student_login, name="student"),
    path("admintemp", admin_views.admintemp, name="admintemp"),
    path("teach", teacher_views.teacher, name="teach"),
    path("stu",student_views.student, name="stu"),
    path("login_view", views.login_view, name="login_view"),
    path("stuview", admin_views. stu_read, name="stuview"),
    path("teachview", admin_views.teach_read, name="teachview"),
    path("studelt/<int:id>/",admin_views.stu_delt, name="studelt"),
    path("teachdelt/<int:id>/", admin_views.teach_delt, name="teachdelt"),
    path("stuupdate/<int:id>/", admin_views.stu_update, name="stuupdate"),
    path("teachupdate/<int:id>/",admin_views.teach_update, name="teachupdate"),
    path("club", admin_views.club, name="club"),
    path("clubview",admin_views.club_views, name="clubview"),
    path("clubdelt/<int:id>/", admin_views.club_delt, name="clubdelt"),
    path("clubupdate/<int:id>/", admin_views.club_update, name="clubupdate"),
    path("viewclub",teacher_views.teach_club_view, name="viewclub"),
    path("event/<int:id>/", teacher_views.create_event, name="event"),
    path("eventview", teacher_views.event_view, name="eventview"),
    path("eventupdate/<int:id>/", teacher_views.event_update, name="eventupdate"),
    path("eventdelt/<int:id>/", teacher_views.event_delt, name="eventdelt"),
    path("not",admin_views.notification, name="not"),
    path("notview",admin_views.not_view, name="notview"),
    path("stunotview",student_views.student_not_view, name="stunotview"),
    path("teachnotview",teacher_views.teach_not_view, name="teachnotview"),
    path("stufeedback", student_views.stu_feedback, name="stufeedback"),
    path("viewfeedback", student_views.feedback_view, name="viewfeedback"),
    path("stueventview", student_views.stu_event_view, name="stueventview"),
    path("adminfeedback", admin_views.admin_feedback_view, name="adminfeedback"),
    path("adminreply/<int:id>/", admin_views.admin_reply, name="adminreply"),

]
