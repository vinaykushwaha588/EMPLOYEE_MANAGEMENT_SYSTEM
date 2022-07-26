from django.shortcuts import redirect, render
from .models import Employee
from .forms import EmployeeForm
# Create your views here.
def employee_view(request):
    data = Employee.objects.all()
    return render(request,'show.html',{'data':data})


def employee_create(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request,'create.html',{'form':form})
    else:
        return render(request,'create.html',{'form':form})

def employee_update(request,eid):
    data = Employee.objects.get(id=eid)
    form = EmployeeForm(request.POST or None, request.FILES or None,instance=data)    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request,'update.html',{'form':form})
    else:
        return render(request,'update.html',{'form':form})


def employee_show(request,eid):
    emp = Employee.objects.get(id=eid)
    print(emp,"<---Get Employee View")
    print(emp.name,emp.email)
    d={'emp':emp}
    return render(request,'showview.html',context=d)


def employee_delete(request,eid):
    data = Employee.objects.get(id=eid)
    data.delete()
    return redirect("/")