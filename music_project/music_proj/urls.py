"""music_proj URL Configuration

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
from django.urls import path, include
# from musicApp import *
from musicApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('musicApp/', include('musicApp.urls')),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('generic/', views.generic, name='generic'),
    path('elements/', views.elements, name='elements'),
    path('home1/', views.home1, name='home1'),
    path('home2/', views.home2, name='home2'),
    path('log_out/', views.log_out, name='log_out'),

    # 소셜 로그인
    path('account/login/kakao/', views.kakao_login, name='kakao_login'),
    path('account/logout/kakao/', views.kakao_logout, name='kakao_logout'),
    path('account/login/kakao/callback/', views.kakao_callback, name='kakao_callback'),

]
