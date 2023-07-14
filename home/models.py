from django.db import models
from datetime import date

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 30)
    desc = models.CharField(max_length = 30)
    date = models.DateField()


    def __str__(self) :
        return self.name

class Admissionform(models.Model):
    rollid = models.IntegerField(primary_key= True)
    name = models.CharField(max_length = 50)
    father_name = models.CharField(max_length = 50)
    education = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 100, default= "Male")
    selectclass = models.CharField(max_length = 500, default="Master")
    date = models.DateField()

    
    def __str__(self) :
        return self.name

 
class Recordfee(models.Model):
    rollid = models.IntegerField(primary_key= True)
    name = models.CharField(max_length = 50)
    fees = models.CharField(max_length = 100)
    selectclass = models.CharField(max_length = 500, default="Master")
    date = models.DateField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100) 
    address = models.CharField(max_length = 100)  
    subject = models.CharField(max_length = 100)  
    date = models.DateField()

    def __str__(self):
       return self.name
                


    