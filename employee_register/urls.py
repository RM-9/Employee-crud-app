from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('',views.employee_form,name='employee_form'),
    path('update/<int:employee_id>',views.employee_update,name='employee_update'),
    path('list/',views.employee_list,name='employee_list'),
    path('delete/<int:employee_id>',views.employee_delete,name='employee_delete'),
]