from django.shortcuts import render
from django.urls import resolve
from .models import Anime, Manga


def home(request):
    page = 'Welcome!'
    anime = Anime.objects.all()
    manga = Manga.objects.all()
    
    context = {'animeOb': anime[:3], 'mangaOb' : manga, 'header' : page}
    return render(request, 'base/home.html', context)

def infoAnimeManga(request, pk):

    pageUrl = resolve(request.path_info).url_name

    if pageUrl == 'AnimPage':
        animeMangaOb = Anime.objects.get(id=pk)

    elif pageUrl == 'MangPage':
        animeMangaOb = Manga.objects.get(id=pk)
    
    #print(resolve(request.path_info).url_name)

    context = {'animeName':animeMangaOb}
    return render(request, 'base/info.html', context)


def loginUser(request):
    current_page = 'login'

    context = {'page' : current_page}
    return render(request, 'base/log_reg_form.html', context)


def registerUser(request):
    return render(request, 'base/log_reg_form.html')



#enjoy the process