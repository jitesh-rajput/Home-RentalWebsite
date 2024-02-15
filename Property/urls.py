from django.contrib import admin
from django.urls import path
from . import views
import index
urlpatterns = [
    path('/home',views.home,name="home"),
    path('/seeproperty',views.seeproperty,name="seeproperty"),
    path('/<int:id>',views.home_review,name="home_review"),
    path("book/<int:id>",views.book,name="book"),
    path("/search",views.search,name="search"),
    path('/profile',views.profile,name='profile'),
     path('/logout', views.logout, name='logout'),
]
