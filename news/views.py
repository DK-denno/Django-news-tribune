from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(response):
    return HttpResponse('Welcome To Moringa Tribune')
