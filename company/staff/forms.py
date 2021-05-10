from django import forms
from .models import Department,Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee,Department
        fields = "__all__"