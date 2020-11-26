from django.shortcuts import render

# Create your views here.

def index(request) :
    # context = {'ment' : '여기까지 잘되시나요?'}
    return render(request, 'index.html')

def elements(request) :
    # context = {'ment' : '여기까지 잘되시나요?'}
    return render(request, 'elements.html')

def generic(request) :
    # context = {'ment' : '여기까지 잘되시나요?'}
    return render(request, 'generic.html')