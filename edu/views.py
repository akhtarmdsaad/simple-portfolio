from django.shortcuts import render

# Create your views here.
def edu(request):
    return render(request,"edu/skills.html",context={"edu":"active"})