import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import resolve
from django.db.models import Q
from .forms import UserCreation
from .models import Anime, Manga, User, UserWatchlist, UserReadlist, WatchlistStatus, ReadlistStatus
from .forms import UserEditForm



def home(request):
    page = 'Welcome!'
    anime = Anime.objects.all()
    manga = Manga.objects.all()
    
    context = {'animeOb': anime[:3], 'mangaOb' : manga[:3], 'header' : page, 'featured_title' : anime[:5]}
    return render(request, 'base/home.html', context)


#implement manga 
def infoAnimeManga(request, pk):
    pageUrl = resolve(request.path_info).url_name
    alreadyinList = False
        
    # Check if page is in anime page
    if pageUrl == 'AnimPage':

        # Get anime from DB
        animeMangaOb = Anime.objects.get(id=pk)

        #Try to find anime in user's watchlist, otherwise return None
        try:    
            user = UserWatchlist.objects.get(user=request.user.id, anime=pk)

        except:
            user = None

    
    elif pageUrl == 'MangPage':
        animeMangaOb = Manga.objects.get(id=pk)

        try:
            user = UserReadlist.objects.get(user=request.user.id, manga=pk)

        
        except:
            user = None
        

    
    if user != None:
        alreadyinList = True

    context = {'animeName': animeMangaOb, 'inList': alreadyinList}
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
    context = {}

    #if user toggles between watchlist to readlist and vice versa (FETCH API CALL)
    if request.method == 'POST':
        context = []
        #get post request from fetch api 
        requestBody = json.loads(request.body)

        
        # check if user wanted to see read list or watchlist
        if requestBody.get('queryType') == 'watchlist':
            userlist = UserWatchlist.objects.filter(user=pk)
            for anList in userlist:
                context.append({'id' : anList.anime.id, 'title': anList.anime.title, 'thumbnail' : anList.anime.large_image, 'status' : anList.status.status_type})

        elif requestBody.get('queryType') == 'readlist':
            userlist = UserReadlist.objects.filter(user=pk)
            for mnList in userlist:
                context.append({'id' : mnList.manga.id, 'title' : mnList.manga.title, 'thumbnail': mnList.manga.large_image, 'status' : mnList.status.status_type})
            

        
        
        
        
        
        jsonContext = json.dumps(context,indent=4, sort_keys=True, default=str)
        
        print(jsonContext)
        
        #Ajax Response 
        return HttpResponse(jsonContext, content_type="application/json")
        

    
    #if user opened his watchlist from menu
    elif request.method == 'GET':
        if 'watchlist' in request.path:
            usersListObject = UserWatchlist.objects.filter(user=pk)
            context = {'list': usersListObject}

        elif 'readlist' in request.path:
            usersListObject = UserReadlist.objects.filter(user=pk)
            context = {'list' : usersListObject}
     
    return render(request, 'base/watchlist_readlist.html', context)

@login_required(login_url='Login')
def catalog(request):
    context = {}
    currentUser = User.objects.get(id=request.user.id)
    
    
    
    
    if 'mangalist' in request.path:
        masterList = Manga.objects.all().order_by('id')
        userReadlistObject = UserReadlist.objects.filter(user=request.user.id)
        mangaListPaginator = Paginator(masterList, 20)
        page_number = request.GET.get('page')
        userReadlist = []

        for counter in userReadlistObject:
            userReadlist.append(counter.manga)

        

        page_object = mangaListPaginator.get_page(page_number)
        context = {'list' : page_object , 'user_list' : userReadlist, 'list_type' : 'manga'}

    elif 'animelist' in request.path:
        masterList = Anime.objects.all()[:100]
        animeListPaginator = Paginator(masterList, 20)
        
        userWatchListObject = UserWatchlist.objects.filter(user=request.user.id)
        userWatchlist = []
        
            
        
        for counter in userWatchListObject:
            userWatchlist.append(counter.anime)
        


        
        page_number = request.GET.get('page')
        page_object = animeListPaginator.get_page(page_number)

        
        
        context = {'list' : page_object, 'user_list' : userWatchlist, 'list_type' : 'anime'}

    
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
    
    context =  {'userProfileObject' : myUser}
    return render(request, "base/profile.html", context)

def editProfile(request):
    userProfile = User.objects.get(id=request.user.id)
    formObject =  UserEditForm(instance=userProfile)

    if request.method == 'POST':
        
        formObject = UserEditForm(request.POST, request.FILES, instance=userProfile)
        if formObject.is_valid():
            formObject.save()
            return redirect('SelfProfile')

        else:
            print(formObject.errors)
    
    context = {'user' : userProfile , 'form' : formObject}
    return render(request, 'base/edit_profile.html', context)

def addtoMyList(request,type,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            

            if type == 'anime':
                userObject = UserWatchlist(user=User.objects.get(id=request.user.id), anime=Anime.objects.get(id=pk),status=WatchlistStatus.objects.get(id=3))
                userObject.save()
                return redirect('AnimeList')
                

            elif type == 'manga':
                userObject = UserReadlist(user=User.objects.get(id=request.user.id), manga=Manga.objects.get(id=pk),status=ReadlistStatus.objects.get(id=1))
                userObject.save()
                return redirect('MangaList')
            
            

    else:
        return redirect('Login')

def dropEntry(request, type, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            if type == 'anime':
                userObject = UserWatchlist.objects.get(user=request.user.id, anime=pk)
                userObject.delete()
                return redirect('AnimeList')

            elif type == 'manga':
                userObject = UserReadlist.objects.get(user=request.user.id, manga=pk)
                userObject.delete()
                return redirect('MangaList')


    

def movetoPlan(request,type, pk):
    
    if type == "manga":
        current_user = UserReadlist.objects.get(user=request.user.id, manga=pk)
        current_user.status = ReadlistStatus.objects.get(id=2)
        #current_user.status = 2
        current_user.save()
        return redirect('ReadList', pk=request.user.id)

    elif type == "anime":
        current_user = UserWatchlist.objects.get(user=request.user.id, anime=pk)
        current_user.status = WatchlistStatus.objects.get(id=3)
        #current_user.status = 3
        current_user.save
        return redirect('WatchList', pk=request.user.id)



def movetoFinish(request, type, pk):
    return HttpResponse('finished', type)

            


        
        
    


# Just enjoy the process.