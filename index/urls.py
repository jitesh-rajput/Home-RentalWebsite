from django.contrib import admin
from django.urls import path
from . import views
import index
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('createnewacc',views.createnewacc,name='createnewacc'),
    path('logout', views.logout, name='logout'),
    path('profile',views.profile,name='profile'),
    path('searchbycity',views.searchbycity,name='searchbycity'),
    path("searchbytype", views.searchbytype, name="searchbytype"),
    path("searchbyprice",views.searchbyprice,name="searchbyprice"),

]
