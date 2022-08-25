from django.shortcuts import render, redirect
from .models import *
from .forms import StudentForm

def index(request):
    return render(request, 'base/index.html')


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }

    return render(request, 'base/student_list.html', context)
    # return render(request, 'base/student_list.html', {'students': students,}) böyle de yazabiliriz

def student_add(request):
    form = StudentForm()
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")


    context = {
        'form': form
    }
    return render(request, 'base/add_student.html', context)


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {
        'form': form,
    }

    return render(request, 'base/update_student.html', context)


def student_delete(request, id):
    student=Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=student)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    context = {
        'student': student,
    }

    return render(request, 'base/delete_student.html', context)

def student_detail(request, id):        
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'base/student_detail.html', context)
