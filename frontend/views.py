from django.shortcuts import render
# Create your views here.
def Homepage(request):
    return render(request,"Frontend_page.html")

def Singlepage(request):
    return render(request,"single_page.html")
