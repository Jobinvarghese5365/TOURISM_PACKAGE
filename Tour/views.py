from django.shortcuts import render, redirect
from Tour.models import PackagesDb,Spot
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def Tour_page(request):
    return render(request,"Backend_page.html")

def Tour_packages(request):
    return render(request, "Add_Packages.html")

def Packages_save(request):
    if request.method =="POST":
        Na = request.POST.get("Name")
        Des = request.POST.get("Description")
        img = request.FILES['image']
        obj = PackagesDb(Name=Na, Description=Des, Image=img)
        obj.save()
        return redirect(Tour_packages)

def update_category(request,c_id):
    if request.method == 'POST':
        a = request.POST.get('Name')
        b = request.POST.get('Description')
        try:
            f = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(f.name,f)
        except MultiValueDictKeyError:
            file = PackagesDb.objects.get(id=c_id).Image
        PackagesDb.objects.filter(id=c_id).update(Name=a,Description=b,Image=file)
        return redirect(Display_Packages)



def Display_Packages(request):
    data = PackagesDb.objects.all()
    return render(request,"Display_Package.html",{'data':data})

def Edit_Packages(request,c_id):
    packages = PackagesDb.objects.get(id=c_id)
    return render(request,"Edit_Packages.html",{'packages': packages})

def Delete_Package(request,c_id):
    data = PackagesDb.objects.get(id=c_id)
    data.delete()
    return redirect(Display_Packages)