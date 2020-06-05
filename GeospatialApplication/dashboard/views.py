from django.shortcuts import render

# Create your views here.

def healthDash(request):
    return render(request,"dashboard/rws.html")