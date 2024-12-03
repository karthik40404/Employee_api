from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=20)
    address=models.TextField()
    experience=models.TextField()
    salary=models.IntegerField()
    phone_no=models.IntegerField()
    position=models.CharField(max_length=20)
    email=models.EmailField()