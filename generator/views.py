import random

from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    character = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        character.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('numbers'):
        character.extend('1234567890')
    if request.GET.get('special'):
        character.extend('!@#$%^&*()')

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(character)
    return render(request, 'generator/password.html', {'password': thepassword})
