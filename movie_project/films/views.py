from django.shortcuts import render

def index(request):
    return render(request, 'films/index.html')

def add_films(request):
    return render(request, 'films/add_films.html')

