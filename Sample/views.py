from django.shortcuts import render

from .forms import studentform

def home(request):
    if request.method =='POST':
        data = studentform(request.POST)

        if data.is_valid():
            data.save()
    context={
        "form":studentform
    }

    return render(request,'home.html',context)

