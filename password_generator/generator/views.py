from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    character = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        character.extend(list('1234567890'))
    length = int(request.GET.get('length', 12))
    the_password = ''
    for x in range(length):
        the_password += random.choice(character)

    return render(request, 'generator/password.html', {'password':the_password})
