from django.shortcuts import render,redirect
from .models import blobmodel
# Create your views here.

def index(request):
    var=blobmodel.objects.all()
    context={'name':var}
    return render(request,'index.html',context)

def update(request,id):
    bloginfo=blobmodel.objects.get(id=id)
    context={'blog':bloginfo}
    if request.method=="POST":
        title=request.POST["title"]
        desc=request.POST["desc"]

        bloginfo.title=title
        bloginfo.desc=desc
        bloginfo.save()
        return redirect('Home')
    return render(request,'update.html',context)

def deletefunc2(request,id):
    del_var=blobmodel.objects.get(id=id)
    del_var.delete()
    return redirect('Home')

def addb(request):
    if request.method=="POST":
        title=request.POST["title"]
        desc=request.POST["desc"]
        
        data=blobmodel(title=title,desc=desc)
        data.save()
        return redirect('Home')

    return render(request,'add.html')
