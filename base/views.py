from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import resolve
from .forms import UserCreation
from .models import Anime, Manga, User


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

    if request.user.is_authenticated:
        return redirect('Home')

    if request.method == 'POST':
        uname = request.POST.get('username-login')
        password = request.POST.get('password-login')

        try:
            user = User.objects.get(username=uname)

        except:
            messages.error(request, 'User not found! Please try again')

        user = authenticate(request, username=uname, password=password)
        

        if user is not None:
            print('success')
            login(request, user)
            return redirect('Home')

        else:
            print('error')
            messages.error(request, 'Login error!')
        

    context = {'page' : current_page}
    return render(request, 'base/log_reg_form.html', context)

def logoutUser(request):
    print('logout')
    logout(request)
    return redirect('Home')



def registerUser(request):
    formObject = UserCreation()

    if request.method == 'POST':
        pass


    context = {'form' : formObject}
    return render(request, 'base/log_reg_form.html', context)





#enjoy the process