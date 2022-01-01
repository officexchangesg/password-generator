from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword=''
    length=int(request.GET.get('length',12))

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get("uppercase"):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get("numbers"):
        characters.extend(list('0123456789'))
    if request.GET.get("specials"):
        characters.extend(list('&#!$=-%'))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html',{'password':thepassword})

# Create your views here.
