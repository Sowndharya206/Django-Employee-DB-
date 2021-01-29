from django.shortcuts import render,redirect
from empreg.forms import Empform
from empreg.models import Emp
# Create your views here.
def empl(request):
    if request.method =="POST":
        form=Empform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                    pass
    else:
        form=Empform()
    return render(request,'index.html',{'form':form}) 
def show(request):  
    emps = Emp.objects.all()  
    return render(request,"show.html",{'emps':emps})  
def edit(request, id):  
    employee = Emp.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Emp.objects.get(id=id)  
    form = Empform(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Emp.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  


