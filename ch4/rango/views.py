from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a> ")

def about(request):
    return HttpResponse("Rango says here is the about page!<br/>This tutorial has been put together by Kenneth Anderson, 2096122a<br/> <a href='/rango/'>Index</a> ")

