"""testeDjango URL Configuration

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
from django.urls import path, include

#importação da home no arquivo views, no APP pages 
from pages.views import pInicial_view, contact_view, profile_view, about_view, feed_view

urlpatterns = [
    path('products/', include('products.urls')),
    path('', pInicial_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('about/', about_view, name='about'),
    path('feed/', feed_view, name='feed'),
    path('contact/', contact_view, name='contact'), #pattern da linha 11
    path('admin/', admin.site.urls),

]
