from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import Admissionform, Contact, Recordfee, Teacher
from django.contrib import messages

# Create your views here.
def index(request):
   
    
    return render(request,("base.html"))


def admission(request):
     if request.method == "POST":
        rollid = request.POST.get('rollid')
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        education = request.POST.get('education')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        selectclass = request.POST.get('selectclass')

        admissionform = Admissionform(rollid = rollid, name= name, father_name = father_name, education = education, city= city, gender = gender, selectclass = selectclass , date = datetime.today())
        admissionform.save()
        messages.success(request, 'Your registration form successfully sent')
        return redirect("/")
        

     return render(request,('admission.html'))    


def studentrecords(request):
   
    alldata = Admissionform.objects.all()
    context = {'studentrecords': alldata}
    return render(request,'Studentrecord.html',context)    

def deleterecord(request, rollid):
    admissionform = Admissionform.objects.get(rollid= rollid)    
    admissionform.delete()
    return redirect("/Studentrecord")

 


def comments(request):
    allcomment = Contact.objects.all()
    context = {'comments': allcomment}
    return render(request, 'comments.html',context)    





def studentfees(request):
    if request.method == "POST":
        rollid = request.POST.get('rollid')
        name = request.POST.get('name')
        fees = request.POST.get('fees')
        selectclass = request.POST.get('selectclass')

        Fee = Recordfee(rollid = rollid, name = name, fees = fees, selectclass = selectclass, date = datetime.today())
        Fee.save()
        messages.success(request, 'Successfully add')
    return render(request,('fees.html'))
        


def adminportal(request):
    return render(request,('adminportal.html'))     

def loginuser(request):
     if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username, password= password)
        
        if user is not None:
    # A backend authenticated the credentials
            login(request,user)
            return redirect ("/adminportal")
     else:


      return render(request,'login.html') 


def logoutuser(request):
    logout(request)
    return redirect("/login") 
    

def timetables(request):
    return render(request,('timetable.html'))  

def teacherlectures(request):
    return render(request,('teacherslecture.html'))     

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc =  request.POST.get('desc')
        contacts = Contact(name = name, email = email,phone = phone, desc = desc , date = datetime.today())
        contacts.save() 
        messages.success (request, 'Your message has been sent')  
    return render(request,('contact.html'))    


def aboutus(request):
    return render(request, ('about.html'))

def aboutstudent(request):
    return render(request, ('aboutstudent.html'))

def aboutteacher(request):
    return render(request, ('aboutteacher.html'))    

def update(request, pk):
    get_data = Admissionform.objects.get(rollid = pk)
   
    return render(request,"editstudentrecord.html",{'key2':get_data})

 
def updatedata(request,pk):
        udata = Admissionform.objects.get(rollid = pk)
        udata.rollid = request.POST['rollid']
        udata.name = request.POST['name']
        udata.father_name = request.POST['father_name']
        udata.education = request.POST['education']
        udata.city = request.POST['city']
        udata.gender = request.POST['gender']
        udata.selectclass = request.POST['selectclass']
        udata.save()
        messages.success(request,'Your record update successfully')
        return redirect('Studentrecord')

def teacherrecord(request):
    teacherdata = Teacher.objects.all()
    context = {'teacherrecord':teacherdata}
    return render(request, 'teacherrecord.html',context)

def Newteacher(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        teacher = Teacher(name = name, phone = phone, address = address, subject = subject, date = datetime.today())
        
        teacher.save()
        messages.success(request,'New teacher record add successfully')
        return redirect("/teacherrecord")
    return render(request,("newteacher.html"))   

def deleteteacher(request, id):
    teacher = Teacher.objects.get(id = id)
    teacher.delete()
    return redirect("/teacherrecord")


def feesrecord(request):
    totalfees = Recordfee.objects.all()
    context = {'feesrecord':totalfees}
    return render(request,'feesrecord.html',context)

def deletefees(request,rollid):
    totalfee = Recordfee.objects.get(rollid = rollid)
    totalfee.delete()
    return redirect('/feesrecord')


def contactdelete(request, id):
    datadelete = Contact.objects.get(id = id)
    datadelete.delete()
    return redirect('/comments')    