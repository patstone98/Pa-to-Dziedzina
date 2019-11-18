from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd


def home(request):
    print('Home')
    return render(request, 'home.html')


def about(request):
    print('About')
    return render(request, 'about.html')


def contact(request):
    print('Contact')
    return render(request, 'contact.html')


def data_analysis(request):
    print('Data analysis')
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

def welon(request):
    print("Welon")
    if request.method=="POST":
        print("Form")

        dane = int(request.POST.get("dane"))
        print(dane)

        if dane == 135:
            skrypt = "<p>Donald Trump</p>"
        elif dane == 145:
            skrypt = "<p>Jarosław Kaczyński</p>"
        elif dane == 146:
            skrypt = "<p>Peter Dinklage</p>"
        return render(request, "dane.html" , {"result_present" : True, "skrypt" : skrypt})
    return render(request, "dane.html")
