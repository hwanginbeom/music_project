from django.shortcuts import render, HttpResponse
from .models import *
from django.template import loader

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
