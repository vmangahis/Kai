import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
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
    

    usersList = User.objects.get(id=request.user.id)

    if pageUrl == 'AnimPage':
        animeMangaOb = Anime.objects.get(id=pk)

    elif pageUrl == 'MangPage':
        animeMangaOb = Manga.objects.get(id=pk)
    

    if animeMangaOb in usersList.watchlist.all() or animeMangaOb in usersList.readlist.all():
        alreadyinList = True

    else:
        alreadyinList = False

    context = {'animeName':animeMangaOb, 'inList': alreadyinList}
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
    if request.method == 'POST':
        formObject = UserCreation(request.POST)
        if formObject.is_valid():
            user = formObject.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('Home')

    
            
    else:
        formObject = UserCreation()




    
    context = {'form' : formObject}
    return render(request, 'base/log_reg_form.html', context)


@login_required(login_url='Login')
@csrf_exempt
def personalList(request, pk):
    #finding user
    usersListObject = User.objects.get(id=pk)

    if request.method == 'POST':

        
        #get post request from fetch api 
        requestBody = json.loads(request.body)

        # check if user wanted to see read list or watchlist
        if requestBody.get('queryType') == 'watchlist':
            genrelistObject = usersListObject.watchlist.all()
           
            
            

        elif requestBody.get('queryType') == 'readlist':
            genrelistObject = usersListObject.readlist.all()

        
        
        genreList = []
        context = []
        
        for x in genrelistObject.all():
            for y in x.genre.values():
                genreList.append(y['name'])
            
            
            context.append({'id': x.id,'title' : x.title, 'genre' : genreList})
            genreList = []
            
            
            
        jsonContext = json.dumps(context,indent=4, sort_keys=True, default=str)
        
        
        return HttpResponse(jsonContext, content_type="application/json")
        

    
    
    elif request.method == 'GET':
        
        if 'watchlist' in request.path:
            context = {'list': usersListObject.watchlist.all()}

        elif 'readlist' in request.path:
            context = {'list' : usersListObject.readlist.all()}
    
    return render(request, 'base/watchlist_readlist.html', context)

@login_required(login_url='Login')
def catalog(request):
    context = {}
    currentUser = User.objects.get(id=request.user.id)
    
    if 'mangalist' in request.path:
        context = {'list' : Manga.objects.all(), 'user_list' : currentUser.readlist.all(), 'list_type' : 'manga'}

    elif 'animelist' in request.path:
        context = {'list' : Anime.objects.all(), 'user_list' : currentUser.watchlist.all(), 'list_type' : 'anime'}

    print(context['user_list'])    
    return render(request, 'base/catalog.html', context)






# Just enjoy the process.