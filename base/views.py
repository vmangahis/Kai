import string
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import resolve
from django.db.models import Q
from .forms import UserCreation
from .models import Anime, Manga, User



def home(request):
    page = 'Welcome!'
    anime = Anime.objects.all()
    manga = Manga.objects.all()
    
    context = {'animeOb': anime[:3], 'mangaOb' : manga[:3], 'header' : page, 'featured_title' : anime[:5]}
    return render(request, 'base/home.html', context)

def infoAnimeManga(request, pk):

    pageUrl = resolve(request.path_info).url_name
    alreadyinList = False
    if request.user.is_authenticated:
        usersList = User.objects.get(id=request.user.id)


    if pageUrl == 'AnimPage':
        animeMangaOb = Anime.objects.get(id=pk)

    elif pageUrl == 'MangPage':
        animeMangaOb = Manga.objects.get(id=pk)
    
    if request.user.is_authenticated:
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
        
        #Ajax Response 
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
    randomSeed = list(string.ascii_lowercase)
    randomSeed.append(string.ascii_uppercase)
    randomSeed.append(string.hexdigits)
    
    if 'mangalist' in request.path:
        masterList = Manga.objects.all()
        mangaListPaginator = Paginator(masterList, 20)
        page_number = request.GET.get('page')

        page_object = mangaListPaginator.get_page(page_number)
        context = {'list' : page_object , 'user_list' : currentUser.readlist.all(), 'list_type' : 'manga', 'seed' : randomSeed}

    elif 'animelist' in request.path:
        masterList = Anime.objects.all()[:100]
        animeListPaginator = Paginator(masterList, 20)

        page_number = request.GET.get('page')
        page_object = animeListPaginator.get_page(page_number)
        
        context = {'list' : page_object, 'user_list' : currentUser.watchlist.all(), 'list_type' : 'anime', 'seed': randomSeed}

    
    return render(request, 'base/catalog.html', context)

def search(request):
    query = request.GET.get('keyword') if request.GET.get('keyword') != None else ''

    manga = Manga.objects.filter(Q(title__icontains=query))
    anime = Anime.objects.filter(Q(title__icontains=query))

    context = {'animeList' : anime, 'mangaList' : manga}

    if query == '':
        print('no search')
        return redirect('Home')

    
    return render(request, 'base/search.html', context)

def profile(request):
    myUser = User.objects.get(id=request.user.id)
    print(myUser)
    context =  {'userProfileObject' : myUser}
    return render(request, "base/profile.html", context)


# Just enjoy the process.