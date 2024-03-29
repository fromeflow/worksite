"""worksite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render
from django.contrib.flatpages import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^private/', include('utils.private_storage.urls')),

    url(r'^accounts/', include('accounts.urls', namespace='accounts', app_name='accounts')),
    url(r'^course/', include('courses.urls', namespace='courses', app_name='courses')),
    url(r'^project/', include('projects.urls', namespace='projects', app_name='projects')),
    url(r'^student/', include('students.urls', namespace='students', app_name='students')),
    url(r'^textbook/', include('textbooks.urls', namespace='textbooks', app_name='textbooks')),

    url(r'^$', lambda r: render(r, 'index.html')),

    url(r'^about/$', views.flatpage, {'url': '/about/'}, name='about'),
]
