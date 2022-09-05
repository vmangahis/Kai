from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('anime/<str:pk>',views.infoAnimeManga ,name='AnimPage'),
    path('manga/<str:pk>',views.infoAnimeManga, name='MangPage'),
    path('login/', views.loginUser, name='Login'),
    path('register/', views.registerUser, name='Register'),
    path('logout/', views.logoutUser, name='Logout'),
    path('watchlist/', views.myWatchList, name='WatchList'),
    path('readlist', views.myReadList, name='ReadList')
]