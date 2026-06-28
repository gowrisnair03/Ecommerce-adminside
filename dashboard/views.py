from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def index(request):
    return render(request, "index.html")

def users(request):
    return render(request,"users.html")

def adduser(request):
    return render(request,"add-user.html")   

def profile(request):
    return render(request,"profile.html")     

def charts(request):
    return render(request,"charts.html")
        

