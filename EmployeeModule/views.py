from django.shortcuts import render, redirect
from django.contrib import messages

from EmployeeModule.forms import EmployeeForm
from EmployeeModule.models import Employee


def employee_form(request,id=0):
  if request.method == 'GET':
      if id ==0:
         form = EmployeeForm()

       else:
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=employee)
       return render(request, 'employee_form.html', {'form': form})
  else:
   if id==0:
      form = EmployeeForm(request.POST)
   else:
       employee = Employee.objects.get(pk=id)
       form = EmployeeForm(request.POST,instance=employee)
   if form.is_valid():
          form.save()
          messages.success(request, 'Registered successfully!')
          return redirect('employee/employee_list/')

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee_list.html', context)
def employee_update(request):
    employee = Employee
    employee_update()
    return redirect('employee/employee_list/')
def employee_delete(request):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee/employee_list/')