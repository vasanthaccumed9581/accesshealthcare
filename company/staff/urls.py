from django.urls import path
from .import views
urlpatterns=[
    path('DepartmentList/',views.Departmentlistview.as_view(),name="Department-list"),
    path('Departmentdetail/<int:pk>',views.Departmentdetailview.as_view(),name="Department-detail"),
    path('createEmployee/',views.Employeecreateview.as_view(),name="Create-Employee"),
    path('thanks/',views.ThanksTemplateview.as_view(),name="form-submitted"),
]