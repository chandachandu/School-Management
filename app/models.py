from django.db import models
from datetime import date,datetime
class adminModel(models.Model):
    admin_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    contact_no=models.IntegerField(unique=True)
    creation_date=models.CharField(max_length=30)




# Create your models here.
class CommonModel(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    contact=models.IntegerField(unique=True)
    subjects=models.CharField()

    class Meta:
        abstract=True

class CoursesModel(models.Model):
    courseid=models.AutoField(primary_key=True)
    coursename=models.CharField(max_length=100)
    courseFee=models.FloatField()

class StudentModel(CommonModel):
    subjects = models.ManyToManyField(CoursesModel)
    fee=models.FloatField()

class FacultyModel(CommonModel):
    subjects = models.ManyToManyField(CoursesModel)
    salary=models.FloatField()
