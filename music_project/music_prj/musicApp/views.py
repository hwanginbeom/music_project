import os
import urllib
from logging import getLogger

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

logger = getLogger(__name__)


def index(request) :
    return render(request, 'musicApp/index.html')

def genre(request) :
    song_meta = SongMeta.objects.all()
    song_meta2 = SongMeta.objects.values()
    # b = SongMeta.objects.get(song_id=1) # 데이터 가져오는 방식
    # gnr = SongMeta.objects.get(song_gn_gnr_basket='GN0500')
    # b = SongMeta.objects.filter(Song_id="0")
    # song = song_meta.filter(song_id = 0)
    print("############################################")
    print(song_meta.values())
    print("############################################")
    print(song_meta.values)
    print("############################################")
    # print(b.album_id) # 가져온 값에서 꺼내는 방식 해당 컬럼명을 가져오면 된다.
    print("############################################")
    print(song_meta2)
    # print(gnr.song_gn_gnr_basket)
    print("#######################39#####################")
    print(song_meta2[0])
    # print(gnr.song_gn_gnr_basket)
    print("#########################42###################")
    print(song_meta2[0]['song_gn_dtl_gnr_basket'])
    # print(gnr.song_gn_gnr_basket)
    print("#########################45###################")
    # for i in song_meta2:
    #     print(i['song_gn_dtl_gnr_basket'])
    print("#########################47###################")
    idx = []
    for i, obj in enumerate(song_meta):
        idx.append(obj)
        # print(obj)
        # print(i)
        if (i == 20):
            break

    # print(obj)
    # id = 0
    # song_id_list = [song_meta[idx[0]].song_id, song_meta[idx[1]].song_id]
    # song_id = song_meta[id].song_id
    # album_id = song_meta[id].album_id
    # artist_id_basket = song_meta[id].artist_id_basket
    # artist_name_basket = song_meta[id].artist_name_basket
    # song_name = song_meta[id].song_name
    # song_gn_gnr_basket = song_meta[id].song_gn_gnr_basket
    # song_gn_dtl_gnr_basket = song_meta[id].song_gn_dtl_gnr_basket
    # issue_date = song_meta[id].issue_date
    # url_link = song_meta[id].url_link
    # album_image = song_meta[id].album_image
    #
    # print(">>>>>>>>>>>>>>>>>>>>" , song_id_list)
    print(">>>>>>>>>>>>>>>>>>>> idx ", len(idx))
    # context = {'song_id': song_id_list, 'album_id' : album_id, 'artist_id_basket' : artist_id_basket,
    #            'artist_name_basket' : artist_name_basket, 'song_name' : song_name, 'song_gn_gnr_basket' : song_gn_gnr_basket,
    #            'song_gn_dtl_gnr_basket' : song_gn_dtl_gnr_basket, 'issue_date' : issue_date, 'url_link' : url_link,
    #            'album_image' : album_image, 'song_meta' : song_meta, 'idx' : idx}
    context = {'idx': idx}
    return render(request, 'musicApp/genre.html', context)

def filtering(request) :
    return render(request, 'musicApp/filtering.html')

def mypage(request) :
    return render(request, 'musicApp/mypage.html')

def new_index(request) :
    song_meta = SongMeta.objects.all()
    # song = song_meta.filter(song_id = 0)
    idx = []
    for i, obj in enumerate(song_meta):
        idx.append(obj)
        if (i == 6):
            break

    print(obj)
    # id = 0
    # song_id_list = [song_meta[idx[0]].song_id, song_meta[idx[1]].song_id]
    # song_id = song_meta[id].song_id
    # album_id = song_meta[id].album_id
    # artist_id_basket = song_meta[id].artist_id_basket
    # artist_name_basket = song_meta[id].artist_name_basket
    # song_name = song_meta[id].song_name
    # song_gn_gnr_basket = song_meta[id].song_gn_gnr_basket
    # song_gn_dtl_gnr_basket = song_meta[id].song_gn_dtl_gnr_basket
    # issue_date = song_meta[id].issue_date
    # url_link = song_meta[id].url_link
    # album_image = song_meta[id].album_image
    #
    # print(">>>>>>>>>>>>>>>>>>>>" , song_id_list)
    print(">>>>>>>>>>>>>>>>>>>> idx ", len(idx))
    # context = {'song_id': song_id_list, 'album_id' : album_id, 'artist_id_basket' : artist_id_basket,
    #            'artist_name_basket' : artist_name_basket, 'song_name' : song_name, 'song_gn_gnr_basket' : song_gn_gnr_basket,
    #            'song_gn_dtl_gnr_basket' : song_gn_dtl_gnr_basket, 'issue_date' : issue_date, 'url_link' : url_link,
    #            'album_image' : album_image, 'song_meta' : song_meta, 'idx' : idx}
    context = {'idx': idx}
    return render(request, 'musicApp/new_index.html', context)

    # return render(request, 'musicApp/new_index.html')

def playlist(request) :
    return render(request, 'musicApp/playlist.html')

def tag(request) :
    return render(request, 'musicApp/tag.html')

def test(request) :
    logger.info('USER_ID=%s', request.user.id)
    print(logger)
    return render(request, 'musicApp/test.html', {'nav_id': 0})


# code 요청
def kakao_login(request):
    app_rest_api_key = '844a2ef702bfa8f3a8f1e3f359924c37'
    redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback/"
    request.session['client_id'] = app_rest_api_key
    request.session['redirect_uri'] = redirect_uri

    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )



def kakao_logout(request):
    # print("70 logout")
    access_token = request.session['access_token']
    # print(access_token)
    requests.post(
        "https://kapi.kakao.com/v1/user/logout",
        headers={"Authorization": f"Bearer {access_token}"},
    )



# access token 요청 함수
@csrf_exempt
def kakao_callback(request):
    print('1단계#########')
    try:
        print('2단계#########')

        app_rest_api_key = '844a2ef702bfa8f3a8f1e3f359924c37'
        redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback/"
        user_token = request.GET.get("code")
        print('81#########')

        # post request
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={app_rest_api_key}&redirect_uri={redirect_uri}&code={user_token}"
        )
        token_response_json = token_request.json()
        # print(token_response_json)
        error = token_response_json.get("error", None)
        print('90#########')

        # if there is an error from token_request
        if error is not None:
            raise KakaoException()
        access_token = token_response_json.get("access_token")
        request.session['access_token'] = access_token
        print('97#########')


        # post request
        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        print('106#########')

        # parsing profile json
        # kakao_account = profile_json.get("kakao_account")
        # print(kakao_account)
        # email = kakao_account.get("email", None)
        kakao_id = profile_json['id']
        # print('#103################')
        # print(email)

        if kakao_id is None:
            raise KakaoException()  # 이메일은 필수제공 항목이 아니므로 수정 필요 (비즈니스 채널을 연결하면 검수 신청 후 필수 변환 가능)
        # profile = kakao_account.get("profile")
        # nickname = profile.get("nickname")
        # profile_image = profile.get("thumbnail_image_url")  # 사이즈 'thumbnail_image_url' < 'profile_image_url'

        try:
            # print('4단계#########')
            # print('109##########')
            user_in_db = UserInfo.objects.get(user_id=kakao_id)
            login(
                request,
                user_in_db,
                backend="django.contrib.auth.backends.ModelBackend",
            )
        except UserInfo.DoesNotExist:
            UserInfo.objects.create(
                user_id=kakao_id,
            )
            UserInfo.set_unusable_password()
            UserInfo.save()
            # after user is saved to db, login the user
            login(
                request,
                UserInfo,
                backend="django.contrib.auth.backends.ModelBackend",
            )
        return redirect("/home2")  # 메인 페이지

    except KakaoException:
        return redirect("/home1")

class KakaoException(Exception):
    pass