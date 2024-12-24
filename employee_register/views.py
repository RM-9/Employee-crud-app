from django.shortcuts import render,redirect
from .forms import Employeeform
from .models import Employee

# Create your views here.
def employee_form(request):
    if request.method=='POST':
        form=Employeeform(request.POST) 
        form.save()
        return  redirect('/employee/list')
    else:        #here we can also write(if request.method=='GET')
        form=Employeeform()
        return render(request,'employee_form.html',{'form':form})

def employee_list(request):
    employeelist=Employee.objects.all()
    return render(request,'employee_list.html',{'employeelist':employeelist})

def employee_update(request,employee_id):
    employee=Employee.objects.get(id=employee_id)
    if request.method=='POST':
        form=Employeeform(request.POST,instance=employee) 
        form.save()
        return  redirect('/employee/list')
    else:
        form=Employeeform(instance=employee)
    return render(request,'employee_form.html',{'form':form})
    
    
def employee_delete(request,employee_id):
    if request.method=='GET':
        employee=Employee.objects.get(id=employee_id)
        employee.delete()
        return  redirect('/employee/list')