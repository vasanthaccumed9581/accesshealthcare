from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    Employeename=models.CharField(max_length=40)
    Department=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20, unique=True, default="", null=False)
    Dateofbirth=models.DateField(blank=True,null=True)
    Picture=models.ImageField(blank=True,null=True,default='0')
    def __str__(self):
        return self.Employeename

class Department(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    Departmentname=models.CharField(max_length=20)
    Manager=models.ForeignKey(Employee,on_delete=models.CASCADE, default='')