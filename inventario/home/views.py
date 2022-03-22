from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcomen.html'
