from cmath import pi
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

# Ths function will add new items and show all items
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        # if fm.is_valid(): 
        #     fm.save() -----> to save all data at one go
             # To save data by field name
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()  # to make all form fields empty after data is subitted
    else:
        fm = StudentRegistration()
    stud = User.objects.all() # To show all data on same page
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

# This function will update/edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})


# This function will delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
