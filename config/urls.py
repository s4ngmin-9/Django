"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from http.client import responses

from django.contrib import admin
from django.http import HttpResponse,Http404
from django.urls import path
from django.shortcuts import render
from bookmark import views

def movies(request):
    movie_title = [
        f"<a href='/movie/{index}/'>{movie['title']}</a>"
        for index, movie in enumerate(movie_list)
    ]
    response_text = '<br>'.join(movie_title)
    return HttpResponse(response_text)

movie_list =[
    {'title':'해리포터와 아즈카반의 죄수','director':'알폰소 쿠아론'},
    {'title':'극한직업','director':'이병헌'},
    {'title':'태극기 휘날리며','director':'강제규'}
]

def movie_detail(request, index):
    if index > len(movie_list) -1:
        raise Http404
    movie = movie_list[index]

    context = {'movie':movie}
    return  render(request,'movie.html',context)


def index(request):
    return HttpResponse("<h1>Sangmin</h1>")

def book_list(request):
    book_text = ''

    return  render(request, 'book_list.html',{'range':range(0,10)})

def book(requset,num):

    return  render(requset,'book_detail.html',context={'num':num})

def languge(requst, lang):
    return HttpResponse(f'<h1> {lang}언어 페이지 <h1>')

def python(requset):
    return HttpResponse('python page')

def gugu(requset,num):
    context = {
        'num':num,
        'results': [num * i for i in range(1,20)]
    }
    return render(requset,'gugu.html',context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/',movies),
    path('movie/<int:index>/', movie_detail),
    path('',index),
    path('book_list/', book_list),
    path('book_list/<int:num>/',book),
    path('languge/<str:lang>/',languge),
    path('languge/python/',python),
    path('gugu/<int:num>/',gugu),
    path('bookmark/',views.bookmark_list),
    path('bookmark/<int:pk>/',views.bookmark_detail),
]