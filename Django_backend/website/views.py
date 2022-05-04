from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'analyse.html')
    form = ImageForm()
    img = Image.objects.all()
    return render(request,'home.html')


def file(request):
    img = Image.objects.all()
    l = len(img)
    x = img[l-1]
    return render(request,'file.html',{'x': x})

def analyse(request):
    return render(request,'analyse.html')

def result(request):
    return render(request,'result.html')

def noresult(request):
    return render(request,'noresult.html')