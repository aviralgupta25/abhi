from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Video_form
from .models import Video

# Create your views here.

def index(request):
    all_video=Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()        
            return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
        form=Video_form()
    return render(request,'home/d1.html',{"form":form,"all":all_video})