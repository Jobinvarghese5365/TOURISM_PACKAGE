from django.shortcuts import render, redirect
from Tour.models import PackagesDb

# Create your views here.
def Tour_page(request):
    return render(request,"Backend_page.html")

def Tour_packages(request):
    return render(request, "Packages.html")

def Packages_save(request):
    if request.method =="POST":
        Na = request.POST.get("Name")
        Des = request.POST.get("Description")
        img = request.FILES['image']
        obj = PackagesDb(Name=Na, Description=Des, Image=img)
        obj.save()
        return redirect(Tour_packages)