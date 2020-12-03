import requests
from allauth.account.views import login, logout
from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from .models import *
# Create your views here.

def index(request) :
    return render(request, 'musicApp/index.html')

def genre(request) :
    return render(request, 'musicApp/genre.html')

def filtering(request) :
    return render(request, 'musicApp/filtering.html')

def mypage(request) :
    return render(request, 'musicApp/mypage.html')

def new_index(request) :
    return render(request, 'musicApp/new_index.html')

def playlist(request) :
    return render(request, 'musicApp/playlist.html')

def tag(request) :
    return render(request, 'musicApp/tag.html')

def test(request) :
    return render(request, 'musicApp/test.html')
