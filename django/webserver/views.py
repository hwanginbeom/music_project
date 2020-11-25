import urllib

from django.shortcuts import render, redirect, get_object_or_404

from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
import requests
from django.shortcuts import redirect


# # code 요청
# def kakao_login(request):
#     app_rest_api_key = '844a2ef702bfa8f3a8f1e3f359924c37'
#     redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback/"
#     return redirect(
#         f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
#     )
#
#
# # access token 요청
# def kakao_callback(request):
#     params = urllib.parse.urlencode(request.GET)
#     return redirect(f'http://127.0.0.1:8000/account/login/kakao/callback?{params}')


class KakaoException(Exception):
    pass


