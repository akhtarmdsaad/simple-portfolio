from django.http import HttpRequest
from django.shortcuts import render,HttpResponse

# Create your views here.
def contact(req):
    return render(req,"contact/contact.html",context={"contact":"active"})