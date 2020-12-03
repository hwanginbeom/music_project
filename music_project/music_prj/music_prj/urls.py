"""music_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from musicApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.new_index, name='new_index'),
    path('genre', views.genre, name='genre'),
    path('filtering', views.filtering, name='filtering'),
    path('mypage', views.mypage, name='mypage'),
    path('new_index', views.new_index, name='new_index'),
    path('playlist', views.playlist, name='playlist'),
    path('tag', views.tag, name='tag'),
    path('test', views.test, name='test'),

]
