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
import ast

from .models import *
from .modeling import *
# Create your views here.

logger = getLogger(__name__)


def index(request) :
    return render(request, 'musicApp/index.html')

def genre(request) :
    balad = SongMeta.objects.filter(song_id__in=[54, 62, 67, 210, 224, 250, 305, 463, 496, 523, 815, 861, 953, 1048, 1053, 1215, 1230, 1236, 1475,1513])
    dancing = SongMeta.objects.filter(song_id__in=[195, 341, 642, 645, 682, 1255, 1313, 1463, 1814, 1816, 2224, 2726, 3220, 3511, 3724, 3727, 3920,3934, 4213, 4491])
    hiphop = SongMeta.objects.filter(song_id__in=[47, 294, 304, 340, 598, 677, 1016, 1290, 1296, 1382, 1471, 1546, 1629, 1659, 1955, 2089, 2148,2214, 2242, 2472])
    rnb = SongMeta.objects.filter(song_id__in=[187, 289, 296, 309, 311, 347, 532, 864, 1182, 1236, 1580, 1632, 1757, 1937, 1938, 2131, 2188, 2230,2267, 2497])
    indie = SongMeta.objects.filter(song_id__in=[19, 47, 148, 229, 309, 363, 677, 788, 1209, 1220, 1232, 1255, 1262, 1632, 1666, 1740, 1856, 1937,2095, 2131])
    rock = SongMeta.objects.filter(song_id__in=[143, 148, 261, 440, 869, 889, 949, 1220, 1262, 1508, 1854, 1954, 2431, 2479, 2955, 3202, 3418,3488, 3514, 3572])
    pop = SongMeta.objects.filter(song_id__in=[109, 198, 255, 299, 307, 398, 420, 466, 501, 706, 787, 805, 846, 863, 961, 964, 972, 989, 1039,1156])
    ost = SongMeta.objects.filter(song_id__in=[32, 146, 152, 353, 463, 632, 646, 671, 800, 1133, 1215, 1421, 2076, 2149, 2188, 2199, 2281, 2312,2332, 2559])
    idol = SongMeta.objects.filter(song_id__in=[67, 642, 645, 682, 861, 889, 1230, 1313, 1814, 1914, 2188, 2224, 2479, 2512, 2726, 3724, 3727,3805, 3934, 4018])
    edm = SongMeta.objects.filter(song_id__in=[14, 174, 397, 595, 699, 956, 1628, 1919, 1966, 2077, 2178, 2209, 3272, 3289, 3499, 3520, 3550,3751, 3874, 4241])
    musical = SongMeta.objects.filter(song_id__in=[28590, 46726, 61591, 71702, 72025, 76938, 85828, 142475, 147574, 167894, 173659, 181297, 183654,201955, 208135, 229524, 237333, 238104, 242683, 247908])
    classic = SongMeta.objects.filter(song_id__in=[186, 378, 667, 752, 1488, 1560, 2069, 2099, 2433, 2820, 2826, 2974, 4188, 4544, 5285, 6012, 6243,6296, 6445, 6522])
    jazz = SongMeta.objects.filter(song_id__in=[453, 818, 902, 1000, 1199, 1238, 1295, 1646, 1828, 1965, 2060, 2110, 2526, 2556, 2617, 2767, 3218,3344, 3362, 3834])

    context = {'balad': balad, 'dancing': dancing, 'hiphop': hiphop, 'rnb': rnb, 'indie': indie, 'rock': rock,
               'pop': pop, 'ost': ost, 'idol': idol, 'edm': edm, 'musical': musical, 'classic': classic, 'jazz': jazz}
    return render(request, 'musicApp/genre.html', context)

def filtering(request) :
    # song_meta = SongMeta.objects.values()
    if request.method == 'POST':
        selected = request.POST.getlist('song_id[]')
        print("#########84###############")
        print(selected)
        print("wow")
        print("###########87#############")
        return render(request, 'musicApp/mypage.html')

    # return redirect(...)
    mood_change = SongMeta.objects.filter(song_id__in=[135153, 569587, 365302, 676338, 177886, 328223, 145616, 529031, 104628, 457585, 601917, 270710, 264357, 672573, 418093, 145174, 352039, 704838, 562575, 260653, 296594, 339513, 548602, 548338, 700011, 83497, 196327, 636401, 486784, 681746, 443095, 420014, 241788, 341206, 439301, 374865, 506919, 5329])
    # print(mood_change.values()[0]['artist_name_basket'][0])
    # x = "['B-EXP', 'I-EXP', 'B-SUB', 'I-SUB', 'O', 'O']"

    array = []
    context = {'mood_change': mood_change, 'array': array}
    return render(request, 'musicApp/filtering.html', context)

def mypage(request) :
    return render(request, 'musicApp/mypage.html')

def new_index(request) :
    pop = SongMeta.objects.filter(song_id__in=[109, 198, 255, 299, 307, 398, 420, 466, 501, 706, 787, 805, 846, 863, 961, 964, 972, 989, 1039, 1156])
    hiphop = SongMeta.objects.filter(song_id__in=[47, 294, 304, 340, 598, 677, 1016, 1290, 1296, 1382, 1471, 1546, 1629, 1659, 1955, 2089, 2148,2214, 2242, 2472])
    indie = SongMeta.objects.filter(song_id__in=[19, 47, 148, 229, 309, 363, 677, 788, 1209, 1220, 1232, 1255, 1262, 1632, 1666, 1740, 1856, 1937,2095, 2131])

    context = {'pop': pop, 'hiphop': hiphop, 'indie': indie}
    return render(request, 'musicApp/new_index.html', context)


def playlist(request) :
    return render(request, 'musicApp/playlist.html')

def tag(request) :
    mood_change = SongMeta.objects.filter(song_id__in=[135153, 569587, 365302, 676338, 177886, 328223, 145616, 529031, 104628, 457585, 601917, 270710, 264357, 672573, 418093, 145174, 352039, 704838, 562575, 260653, 296594, 339513, 548602, 548338, 700011, 83497, 196327, 636401, 486784, 681746, 443095, 420014, 241788, 341206, 439301, 374865, 506919, 5329])
    rest = SongMeta.objects.filter(song_id__in=[464051, 11657, 623820, 7605, 211063, 563620, 528972, 339513, 410108, 612944, 206254, 5932, 71842, 554751, 34258,93405, 32120, 38545, 428898, 40025, 165942, 314714, 266399, 502078, 529031, 227094, 175362, 538566, 457585, 470129,689258, 476458, 175418, 571016, 266079, 402769, 244233, 625875, 247969])
    windless = SongMeta.objects.filter(song_id__in=[221629, 297450, 587323, 554774, 266241, 135133, 649023, 294936, 221482, 379154, 1133, 528571, 481327, 357997,448847, 179692, 376039, 270762, 688674, 413389, 614659, 487219, 620800, 569687, 415372, 67275, 23090, 585338,647498, 217209, 96922, 679075, 413231, 290387, 557540, 168642, 439003, 183468])
    pop = SongMeta.objects.filter(song_id__in=[672232, 430846, 264908, 588165, 19486, 668733, 428272, 284554, 319715, 669677, 597714, 100733, 662538, 57072, 95554, 140638, 17573, 624848, 205757, 12397, 58393, 243951, 207558, 33996, 470, 41677, 177460, 424929, 296035, 671650, 355067, 700994, 383011, 582134, 462001, 374954, 550695, 645161, 200711])
    night = SongMeta.objects.filter(song_id__in=[282155, 390973, 161304, 281488, 371473, 82671, 58828, 439812, 465369, 490923, 29793, 162918, 143837, 472296, 28266, 556317, 484234, 383011, 115662, 327327, 246735, 13198, 665202, 592526, 571016, 559881, 59482, 547, 616207, 58994, 507045, 35945, 156468, 591123, 241700, 287902, 582372, 126694, 175230])
    emotion = SongMeta.objects.filter(song_id__in=[13815, 366786, 454528, 451593, 61159, 231078, 608386, 701981, 555338, 691256, 38876, 621653, 202564, 547185, 529618, 667394, 9588, 96310, 703435, 8719, 629092, 51770, 90947, 278907, 640753, 555029, 683520, 27469, 342835, 367935, 75971, 278995, 332377, 549768, 693256, 625996, 543094, 611737, 581784])
    healing = SongMeta.objects.filter(song_id__in=[481910, 216728, 460884, 547506, 541420, 106365, 288472, 226792, 312471, 608717, 201186, 611442, 389446, 92356, 194190, 393884, 601517, 573989, 322117, 287050, 81937, 656573, 568920, 416583, 590016, 62736, 75909, 554702, 473953, 143631, 624489, 521544, 641599, 253855, 545162, 649108, 112223, 222618])
    dawn = SongMeta.objects.filter(song_id__in=[527024, 706177, 327975, 86242, 427965, 529664, 302047, 162485, 567991, 97942, 574649, 447666, 323882, 368237, 24460, 660685, 263018, 366617, 352739, 394079, 371698, 205060, 339802, 364875, 515999, 269965, 649432, 611203, 683357, 163560, 599327, 187066, 219072, 132247, 553831, 383722, 461673, 78756])
    cafe = SongMeta.objects.filter(song_id__in=[195197, 487343, 434533, 105845, 433543, 455833, 269000, 244700, 538419, 31258, 46875, 563003, 123344, 207743, 526507, 492005, 384450, 313438, 293911, 496275, 175262, 509949, 666278, 333768, 262019, 232963, 12965, 73440, 191309, 152870, 92727, 706765, 184543, 462208, 587659, 698935, 480455, 106739])
    ballade = SongMeta.objects.filter(song_id__in=[82330, 515325, 405668, 80209, 166665, 104260, 150714, 529965, 448618, 629980, 418859, 369686, 46162, 439409, 90465, 580074, 518960, 587291, 222763, 357238, 248401, 332442, 346161, 83623, 104703, 225228, 193354, 448698, 516237, 71385, 141998, 410571, 456665, 300444, 254889, 549966, 475635, 635537])
    store_music = SongMeta.objects.filter(song_id__in=[29280, 86068, 621367, 654391, 684683, 147115, 579896, 153045, 158338, 512170, 276612, 566598, 610851, 478957, 590253, 157636, 379163, 590977, 307672, 44782, 506454, 524977, 575062, 696317, 631591, 251582, 160505, 174104, 201714, 169440, 559607, 285099, 611946, 55553, 359133, 280879, 369649, 646175])
    exciting = SongMeta.objects.filter(song_id__in=[135153, 569587, 365302, 676338, 177886, 328223, 145616, 529031, 104628, 457585, 601917, 270710, 264357, 672573, 418093, 145174, 352039, 704838, 562575, 260653, 296594, 339513, 548602, 548338, 700011, 83497, 196327, 636401, 486784, 681746, 443095, 420014, 241788, 341206, 439301, 374865, 506919, 5329])
    drive = SongMeta.objects.filter(song_id__in=[123974, 134081, 504052, 131476, 182756, 388758, 96773, 598740, 467087, 429998, 477817, 377576, 224430, 266614, 122363, 421683, 585999, 451489, 116059, 274313, 562075, 657907, 183579, 55540, 367459, 11611, 624031, 130275, 100899, 423807, 125237, 55279, 279151, 619811, 333429, 551411, 615368, 24087])



    print(rest)
    # print(song_meta.values())
    context = {'mood_change': mood_change, 'rest': rest, 'windless': windless, 'pop': pop, 'night': night, 'emotion': emotion,
               'healing':healing, 'dawn': dawn, 'cafe': cafe, 'ballade': ballade, 'store_music': store_music, 'exciting': exciting, 'drive': drive}
    return render(request, 'musicApp/tag.html', context)

def test(request) :
    logger.info('USER_ID=%s', request.user.id)
    print(logger)

    if request.method == 'POST':
        selected = request.POST.getlist('song_id[]')
        with open('C:/Users/hwang in beom/Desktop/final/50000' + '/val2.json', encoding="utf-8") as f:
            val2 = json.load(f)
        val2[0]['songs'] = selected
        # write_json(self.answers, 'results50000.json')
        print(selected)
        print("#########84###############")
        print(val2)
        print("wow")
        print("###########87#############")
        # FILE_PATH = './dataset'
        render(request, 'musicApp/test.html')
        U_space = PlaylistEmbedding('C:/Users/hwang in beom\Desktop/final/50000')
        U_space.write_json(val2,'val2.json')
        print("############179##############")
        U_space.run()
        print("############181##############")
        print(U_space.answers[0]['songs'][0:10])
        print("############183##############")
        song_data = U_space.answers[0]['songs'][0:10]
        select_song = SongMeta.objects.filter(
            song_id__in=song_data)
        context = {'select_song': select_song }

        return render(request, 'musicApp/mypage.html', context)

    return render(request, 'musicApp/test.html')


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