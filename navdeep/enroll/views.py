from django.shortcuts import render,HttpResponseRedirect
from .forms import fo
from .models import add
from django.contrib import messages


# Create your views here.
def addandshow(request):
    if request.method =="POST":
        fm=fo(request.POST)
        if fm.is_valid():
            fm.save()
            fm=fo()
            messages.success(request, "Successfully added name")
    else:
        fm=fo()


    return render(request,'enroll/addandshow.html',{"form":fm})


def home(request):
    return render(request,'enroll/home.html')


def delete(request,id):
    if request.method=="POST":
        s=add.objects.get(pk=id)
        s.delete()
        return HttpResponseRedirect('/show')



def update(request,id):
    if request.method=="POST":
        pi=add.objects.get(id=id)
        fm=fo(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = add.objects.get(id=id)
        fm = fo( instance=pi)
    return render(request,'enroll/update.html',{"formd":fm})


def show(request):
    stud=add.objects.all()
    return render(request,'enroll/show.html',{"stud":stud})

def search(request):
    if request.method=="POST":
        search=request.POST.get("name")
        post=add.objects.filter(name__icontains=search)
    return render(request,'enroll/showname.html',{'p':post})