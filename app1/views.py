from django.shortcuts import render,redirect

# Create your views here.
from app1.models import Student
from app1.form import std_form
from django.http import HttpResponse
from app1.form import student_delete_form

def std_list(request):
    data=Student.objects.all()
    form=std_form()
    if request.method=='POST':
        form=std_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    return render(request,'std_list.html',{'data':data,'form':form})


def std_update(request,id):
    student=Student.objects.get(id=id)
    form=std_form(instance=student)
    if request.method=="POST":
        form=std_form(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    return render(request,'std_update.html',{'form':form})

def std_delete(request,id):
    def_user="shreeya"
    def_password="1234"
    std=Student.objects.get(id=id)
    del_form=student_delete_form()
    if request.method=='POST':
        del_form=student_delete_form(request.POST)
        if del_form.is_valid():
            user=del_form.cleaned_data['username']
            password=del_form.cleaned_data['password']
            if user==def_user and password==def_password:
                std.delete()
                return redirect('home_page')
            else:
                return HttpResponse('<h1>Invalid username/password</h1>')
    return render(request,'delete_std.html',{'del_form':del_form})

