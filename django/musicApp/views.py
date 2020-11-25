import urllib

from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from webserver.views import KakaoException
from .models import *
from django.template import loader
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
import requests
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here

# def index(request) :   #HttpResponse는 혼자 바로 응답, render는 템플릿 통해 응답
#     # return HttpResponse('<div align=center>섭이와 함께하는 장고</div>')
#     return render(request, 'hello/index.html')

def hi(request) :
    context = {'ment' : '여기까지 잘되시나요?'}
    return render(request, 'hello/ok.html',context)

def wow(request) :
    # context = {'ment' : '여기까지 잘되시나요?'}
    return render(request, 'musicapp/index.html')

def popup(request) :
    # context = {'ment' : '여기까지 잘되시나요?'}
    return render(request, 'musicapp/oauth.html')


def login(request):
    if request.method == 'POST':
        id = request.POST['id']
        pwd = request.POST['pwd']

        user = TestUser.objects.get(user_id = id)
        context = {}
        if user is not None:
            context['user'] = user
        return render(request, 'hello/success.html',context)
    return HttpResponse('장고 프레임워크')




def index(request):
    template = loader.get_template('musicapp/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

# code 요청
def kakao_login(request):
    app_rest_api_key = '844a2ef702bfa8f3a8f1e3f359924c37'
    redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback/"
    request.session['client_id'] = app_rest_api_key
    request.session['redirect_uri'] = redirect_uri

    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
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

        # post request
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={app_rest_api_key}&redirect_uri={redirect_uri}&code={user_token}"
        )
        token_response_json = token_request.json()
        print(token_response_json)
        error = token_response_json.get("error", None)

        # if there is an error from token_request
        if error is not None:
            raise KakaoException()
        access_token = token_response_json.get("access_token")


        # post request
        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        print("#88")
        print(profile_request)
        profile_json = profile_request.json()
        print("#96")
        print(profile_json)
        print(profile_json['id'])
        # parsing profile json
        kakao_account = profile_json.get("kakao_account")
        print(kakao_account)
        email = kakao_account.get("email", None)
        kakao_id = profile_json['id']
        # kakao_account = profile_json.get("kakao_account")
        # email = kakao_account.get("email", None)
        # email = kakao_account.get("email", None)
        print('#103################')
        print(email)

        if kakao_id is None:
            print('3단계#########')

            raise KakaoException()  # 이메일은 필수제공 항목이 아니므로 수정 필요 (비즈니스 채널을 연결하면 검수 신청 후 필수 변환 가능)
        # profile = kakao_account.get("profile")
        # nickname = profile.get("nickname")
        # profile_image = profile.get("thumbnail_image_url")  # 사이즈 'thumbnail_image_url' < 'profile_image_url'

        try:
            print('4단계#########')
            print('109##########')
            user_in_db = UserInfo.objects.get(user_id=kakao_id)
            print('111##########')

            # # kakao계정 email이 서비스에 이미 따로 가입된 email 과 충돌한다면
            # if user_in_db.user_type != 'kakao':
            #     print('113##########')
            #     raise KakaoException()
            # # 이미 kakao로 가입된 유저라면
            # else:
            print('117##########')
            # 서비스에 rest-auth 로그인
            # data = {'code': user_token, 'access_token': access_token}
            # accept = requests.post(
            #     f"http://127.0.0.1:8000/account/login/kakao/todjango", data=data
            # )
            # accept_json = accept.json()
            # accept_jwt = accept_json.get("token")

            # 프로필 정보 업데이트
            UserInfo.objects.filter(user_id=kakao_id).update(
                # realname=nickname,                user_id = kakao_id
                                                    email='abc',
                                                    user_id = kakao_id,
                                                    # age_group=gender,
                                                    # profile_image=profile_image,
                                                    # is_active=True
                                                    )
            # UserInfo.objects.filter(email=email).update(realname=nickname,
            #                                             email=email,
            #                                             user_type='kakao',
            #                                             profile_image=profile_image,
            #                                             is_active=True
            #                                             )

        except UserInfo.DoesNotExist:
            # 서비스에 rest-auth 로그인
            # data = {'code': user_token, 'access_token': access_token}
            # print('150##########')
            # accept = requests.post(
            #     f"http://127.0.0.1:8000/account/login/kakao/todjango", data=data
            # )
            # print('154##########')
            # print(accept)
            # print('156##########')
            #
            # # print(accept2)
            # print('154##########')
            # accept_json = accept.json()
            # accept_jwt = accept_json.get("token")
            UserInfo.objects.create(
                                                    # realname=nickname,
                                                    user_id = kakao_id,
                                                    email = 'abc',
                                                    # user_type='kakao',
                                                    # profile_image=profile_image,
                                                    # is_active=True
                                                    )
        return redirect("http://127.0.0.1:8000/musicApp/wow/")  # 메인 페이지

    except KakaoException:
        return redirect("http://127.0.0.1:8000/account/login/kakao/")

@csrf_exempt
class KakaoToDjangoLogin(SocialLoginView):
    adapter_class = kakao_views.KakaoOAuth2Adapter
    client_class = OAuth2Client

# def kakao_login(request):
#     app_rest_api_key = '844a2ef702bfa8f3a8f1e3f359924c37'
#     redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback/"
#     # app_rest_api_key = os.environ.get("KAKAO_REST_API_KEY")
#     # redirect_uri = main_domain + "users/login/kakao/callback"
#     return redirect(
#         f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
#     )
#
#
# class KakaoException(Exception):
#     pass
#
# # https://developers.kakao.com/docs/restapi/user-management
# def kakao_callback(request):
#     try:
#         # app_rest_api_key = os.environ.get("KAKAO_REST_API_KEY")
#         # redirect_uri = main_domain + "users/login/kakao/callback"
#         app_rest_api_key = '844a2ef702bfa8f3a8f1e3f359924c37'
#         redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback/"
#         user_token = request.GET.get("code")
#         # post request
#         token_request = requests.get(
#             f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={app_rest_api_key}&redirect_uri={redirect_uri}&code={user_token}"
#         )
#
#         token_response_json = token_request.json()
#         error = token_response_json.get("error", None)
#         # if there is an error from token_request
#         if error is not None:
#             raise KakaoException()
#         access_token = token_response_json.get("access_token")
#         profile_request = requests.get(
#             "https://kapi.kakao.com/v2/user/me",
#             headers={"Authorization": f"Bearer {access_token}"},
#         )
#         profile_json = profile_request.json()
#         # print(profile_json)
#         # parsing profile json
#         kakao_account = profile_json.get("kakao_account")
#         email = kakao_account.get("email", None)
#         if email is None:
#             raise KakaoException()
#         profile = kakao_account.get("profile")
#         # nickname = profile.get("nickname")
#         # profile_image_url = profile.get("profile_image_url")
#         try:
#             user_in_db = models.UserInfo.objects.get(email=email)
#             if user_in_db.register_login_method != models.UserInfo.REGISTER_LOGIN_KAKAO:
#                 raise KakaoException()
#             else:
#                 login(
#                     request,
#                     user_in_db,
#                     backend="django.contrib.auth.backends.ModelBackend",
#                 )
#         except models.UserInfo.DoesNotExist:
#             new_user_to_db = models.UserInfo.objects.create(
#                 user_id=email,
#                 email=email,
#                 # first_name=nickname,
#                 # register_login_method=models.UserInfo.REGISTER_LOGIN_KAKAO,
#                 # email_confirmed=True,
#             )
#             # https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.set_unusable_password
#             new_user_to_db.set_unusable_password()
#             new_user_to_db.save()
#             # after user is saved to db, login the user
#             login(
#                 request,
#                 new_user_to_db,
#                 backend="django.contrib.auth.backends.ModelBackend",
#             )
#         return redirect("http://127.0.0.1:8000/musicApp/wow")
#     except KakaoException:
#         return redirect("http://127.0.0.1:8000/account/login/kakao/")