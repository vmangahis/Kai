import json
import cloudinary
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
from .models import Activities,ActivityStatus, ActivityType,Anime, Manga, User, UserWatchlist, UserReadlist, WatchlistStatus, ReadlistStatus
from .forms import UserEditForm



def home(request):
    page = 'Welcome!'
    anime = Anime.objects.all()
    manga = Manga.objects.all()
    
    context = {'animeOb': anime[:3], 'mangaOb' : manga[:3], 'header' : page, 'featured_title' : anime[:5]}
    return render(request, 'base/home.html', context)


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
        masterList = Anime.objects.all().order_by('id')
        animeListPaginator = Paginator(masterList, 10)
        
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
    context = {}
    manga = Manga.objects.filter(Q(title__icontains=query))
    anime = Anime.objects.filter(Q(title__icontains=query))
    
    if anime.count() > 5:
        context.update({'animeList' : anime[:5], 'viewAllAnime' : True})

    else:
        context.update({'animeList' : anime, 'viewAllAnime' : False})


    if manga.count() > 5:
        context.update({'mangaList' : manga[:5], 'viewAllManga' : True})

    else:
        context.update({'mangaList' : manga , 'viewAllManga' : False})

    

    if query == '':
        return redirect('Home')

    
    return render(request, 'base/search.html', context)

def fullResult(request, type):
    key = request.GET.get('keyword')
    context = {}
    if type == "manga":
        resultObject = Manga.objects.filter(Q(title__icontains=key))
        
    elif type == 'anime':
        resultObject = Anime.objects.filter(Q(title__icontains=key))

    context.update({'list' : resultObject, 'pageType' : type})
    return render(request, "base/full_result.html", context)


def profile(request):
    myUser = User.objects.get(id=request.user.id)

    watchlist = UserWatchlist.objects.filter(user=request.user.id)
    readlist = UserReadlist.objects.filter(user=request.user.id)
    activities = Activities.objects.filter(user=request.user.id).order_by('-timestamp')[:5]
    
    context =  {'userProfileObject' : myUser, 'watchlist' : watchlist, 'readlist': readlist, 'activities': activities}
    return render(request, "base/profile.html", context)

def editProfile(request):
    #Get current user
    userProfile = User.objects.get(id=request.user.id)

    #Initialize form with the current user's data
    formObject =  UserEditForm(instance=userProfile)


    #Upon submission of form
    if request.method == 'POST':
        
        formObject = UserEditForm(request.POST, request.FILES, instance=userProfile)

        #Validation of edit form
        if formObject.is_valid():

            if len(request.FILES) != 0:
                upload = cloudinary.uploader.upload(formObject.cleaned_data['avatar'],folder=f"user/{userProfile.id}/", unique_filename=True)

            #Check if user has previous image
                if userProfile.avatar_public_id is not None:
                    delete_image_id = userProfile.avatar_public_id
                    deleteimage = cloudinary.uploader.destroy(delete_image_id, invalidate=True)
                

                userProfile.avatar_url = upload['secure_url']
                userProfile.avatar_public_id = upload['public_id']
                userProfile.avatar = f'/{upload["public_id"]}.{upload["format"]}'
            formObject.save()
            
            
            return redirect('SelfProfile')

        else:
            print(formObject.errors)
    
    context = {'user' : userProfile , 'form' : formObject}
    return render(request, 'base/edit_profile.html', context)

#Adding entry (Default "Watching/Reading Status")
def addtoMyList(request,type,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            if type == 'anime':
                userObject, alreadyExists = UserWatchlist.objects.get_or_create(user=User.objects.get(id=request.user.id), anime=Anime.objects.get(id=pk))
                userObject.status = WatchlistStatus.objects.get(id=2)
                activitiesObject = Activities.objects.create(user=User.objects.get(id=request.user.id), activity_type=ActivityType.objects.get(id=2), title=Anime.objects.get(id=pk).title, title_id=pk, activity_status=ActivityStatus.objects.get(status="ACTIVE"), activity_thumbnail=Anime.objects.get(id=pk).thumbnail)
                activitiesObject.save()
                userObject.save()

                if alreadyExists:
                    return redirect('WatchList', pk=request.user.id)

                else:
                    return redirect('AnimeList')
                

            elif type == 'manga':

                userObject, alreadyExists = UserReadlist.objects.get_or_create(user=User.objects.get(id=request.user.id), manga=Manga.objects.get(id=pk))
                userObject.status = ReadlistStatus.objects.get(id=1)
                activitiesObject = Activities.objects.create(user=User.objects.get(id=request.user.id), activity_type=ActivityType.objects.get(id=1), title=Manga.objects.get(id=pk).title, title_id=pk, activity_status=ActivityStatus.objects.get(status="ACTIVE"), activity_thumbnail=Manga.objects.get(id=pk).thumbnail)
                activitiesObject.save()
                userObject.save()
                if alreadyExists:
                    return redirect('ReadList', pk=request.user.id)
                
                else:
                    return redirect('MangaList')
            
            

    else:
        return redirect('Login')

#Deleting entry
def dropEntry(request, type, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            if type == 'anime':
                userObject = UserWatchlist.objects.get(user=request.user.id, anime=pk)
                userObject.delete()
                return redirect('WatchList', pk=request.user.id)

            elif type == 'manga':
                userObject = UserReadlist.objects.get(user=request.user.id, manga=pk)
                userObject.delete()
                return redirect('ReadList', pk=request.user.id)


    

def movetoPlan(request,type, pk):
    
    if type == "manga":
        current_user = UserReadlist.objects.get(user=request.user.id, manga=pk)
        current_user.status = ReadlistStatus.objects.get(id=2)
        activitiesObject = Activities.objects.create(user=User.objects.get(id=request.user.id), activity_type=ActivityType.objects.get(id=1), title=Manga.objects.get(id=pk).title, title_id=pk, activity_status=ActivityStatus.objects.get(status="PLAN"), activity_thumbnail=Manga.objects.get(id=pk).thumbnail)
        activitiesObject.save()
        current_user.save()
        return redirect('ReadList', pk=request.user.id)

    elif type == "anime":
        current_user = UserWatchlist.objects.get(user=request.user.id, anime=pk)
        current_user.status = WatchlistStatus.objects.get(id=3)
        activitiesObject = Activities.objects.create(user=User.objects.get(id=request.user.id), activity_type=ActivityType.objects.get(id=2), title=Anime.objects.get(id=pk).title, title_id=pk, activity_status=ActivityStatus.objects.get(status="PLAN"), activity_thumbnail=Anime.objects.get(id=pk).thumbnail)
        activitiesObject.save()
        current_user.save()
        return redirect('WatchList', pk=request.user.id)



def movetoFinish(request, type, pk):
    
    if type == "manga":
        current_user = UserReadlist.objects.get(user=request.user.id, manga=pk)
        current_user.status = ReadlistStatus.objects.get(id=3)
        activitiesObject = Activities.objects.create(user=User.objects.get(id=request.user.id), activity_type=ActivityType.objects.get(id=1), title=Manga.objects.get(id=pk).title, title_id=pk, activity_status=ActivityStatus.objects.get(status="COMPLETED"), activity_thumbnail=Manga.objects.get(id=pk).thumbnail)
        activitiesObject.save()
        current_user.save()

        return redirect('ReadList', pk=request.user.id)

    elif type == "anime":
        current_user = UserWatchlist.objects.get(user=request.user.id, anime=pk)
        current_user.status = WatchlistStatus.objects.get(id=1)
        activitiesObject = Activities.objects.create(user=User.objects.get(id=request.user.id), activity_type=ActivityType.objects.get(id=2), title=Anime.objects.get(id=pk).title, title_id=pk, activity_status=ActivityStatus.objects.get(status="COMPLETED"), activity_thumbnail=Anime.objects.get(id=pk).thumbnail)
        activitiesObject.save()
        current_user.save()

        return redirect('WatchList', pk=request.user.id)

            


        
        
    


# Just enjoy the process.