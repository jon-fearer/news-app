"""news_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from news_app import views as app_views

urlpatterns = [
    path('admin', admin.site.urls, name='admin'),
    path('', app_views.login_view, name='login_view'),
    path('home', app_views.home, name='home'),
    path('logout', app_views.logout_view, name='logout_view'),
    path('log_user_query', app_views.log_user_query, name='log_user_query'),
    path('favicon.ico', app_views.favicon_view, name='favicon_view')
]
