from django.shortcuts import render
from Tour.models import PackagesDb,Spot
# Create your views here.
def Homepage(request):
    pro = PackagesDb.objects.all()
    return render(request,"Frontend_page.html",{'pro':pro})

def Singlepage(request,id):
    data = PackagesDb.objects.filter(id=id)
    x = Spot.objects.filter(Destination__id=id)

    return render(request,"single_page.html",{'data':data,'x':x})

def Destination(request):
    return render(request,"destination_single.html")