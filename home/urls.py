from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    
    path("", views.index, name = 'home'),
    path("admission", views.admission, name = 'admission'),
    path("Studentrecord", views.studentrecords, name = 'Studentrecord'),
    path("adminportal", views.adminportal, name = 'adminportal'),
    path("timetable", views.timetables, name = 'timetable'),
    path("teacherslecture", views.teacherlectures, name = 'teacherslecture'),
    path("contact", views.contacts, name = 'contact'),
    path("login", views.loginuser, name = 'login'),
    path("logout", views.logoutuser, name = 'logout'),
    path("comments", views.comments, name = 'comments'),
    path("about", views.aboutus, name = 'about'),
    path("aboutstudent", views.aboutstudent, name = 'aboutstudent'),
    path("aboutteacher", views.aboutteacher, name = 'aboutteacher'),
    path("fees", views.studentfees, name = 'fees'),
    path('delete/<int:rollid>', views.deleterecord, name = 'delete'),
    path('editstudentrecord/<int:pk>', views.update, name = 'editstudentrecord'),
    path('update/<int:pk>', views.updatedata, name = 'update'),
    path('teacherrecord', views.teacherrecord, name = 'teacherrecord'),
    path("newteacher", views.Newteacher, name = 'newteacher' ),
    path ('teacherrecord/<int:id>',views.deleteteacher, name = 'teacherrecord'),
    path("feesrecord", views.feesrecord, name = 'feesrecord' ),
    path('feesrecord/<int:rollid>',views.deletefees, name = 'feesrecord'),
    path('comments/<int:id>',views.contactdelete, name = 'comments'),

  
    

]
