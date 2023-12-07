from django.shortcuts import render
from .models import Film, Genre


def index(request):
    films = Film.objects('-year')
    genres = Genre.objects.all()
    context = {'films': films, 'genres': genres}
    return render(request, 'index.html', context)