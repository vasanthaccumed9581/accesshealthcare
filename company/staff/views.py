from django.shortcuts import render
from .models import Department,Employee
import datetime
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

class Departmentlistview(ListView):
    model=Department
    template_name = 'staff/Department_list.html'
    context_object_name = 'Departments'

class Departmentdetailview(DetailView):
    model = Department
    template_name = 'staff/department_detail.html'
    context_object_name = 'department'

class Employeecreateview(CreateView):
    model=Employee
    fields =["Employeename","Department","Email","Picture","Dateofbirth"]
    success_url ='/staff/thanks/'

class ThanksTemplateview(TemplateView):
    template_name ='staff/thanks.html'