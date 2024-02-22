from django.shortcuts import render,redirect
from .forms import contactForm
from  . import models,forms

# Create your views here.

def DjangoForm(request):
    form=contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'django_form.html',{'form':form})


def DjangoModel(request):
    student= models.Student.objects.all()
    return render(request,'django_model.html',{'data':student})

def delete_student(request, roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect("django_Model")



def add_student(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.StudentForm()
    return render(request, 'add_student.html', {'form' : form})