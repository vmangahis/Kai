from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('anime/<str:pk>',views.infoAnimeManga ,name='AnimPage'),
    path('manga/<str:pk>',views.infoAnimeManga, name='MangPage'),
    path('login/', views.loginUser, name='Login'),
    path('register/', views.registerUser, name='Register'),
    path('logout/', views.logoutUser, name='Logout'),
    path('watchlist/<str:pk>', views.personalList, name='WatchList'),
    path('readlist/<str:pk>', views.personalList, name='ReadList'),
    path('animelist/', views.catalog, name='AnimeList'),
    path('mangalist/', views.catalog, name='MangaList'),
    path('search/', views.search, name='Search'),
    path('profile/', views.profile, name='SelfProfile'),
    path('profile/edit', views.editProfile, name='EditProfile'),
    path('addtolist/<str:type>/<str:pk>', views.addtoMyList, name='addtolist'),
    
]




