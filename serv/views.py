from django.shortcuts import render

# Create your views here.
def services(req):  
    return render(req,"serv/services.html",context={"services":"active"})