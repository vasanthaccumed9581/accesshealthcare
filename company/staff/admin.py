from django.contrib import admin

# Register your models here.
from .models import Employee,Department

class MyEmployeeadmin(admin.ModelAdmin):
    list_display = ["id","Employeename","Department","Email","Picture","Dateofbirth"]

admin.site.register(Employee,MyEmployeeadmin)

class MyDepartmentadmin(admin.ModelAdmin):
    list_display =["Departmentname","Manager"]

admin.site.register(Department,MyDepartmentadmin)
