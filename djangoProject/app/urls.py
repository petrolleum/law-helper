"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from app import views

urlpatterns = [
    path('law_query/', views.law_query, name='law_query'),
    path('judgement_query/', views.judgement_query, name='judgement_query'),
    path('image/<str:image_name>/', views.getImageByUrl, name='getImageByUrl'),
    path('getLawByNum/',views.getLawByNum,name='getLawByNum'),
    path('getLawByContent/',views.getLawByContent,name='getLawByContent'),
    path('getFactByKeyWord/',views.getFactByKeyWords,name='getFactByKeyWord'),
    path('getJudgements/',views.getJudgements,name='getJudgement'),
    path('getJudgement/',views.getJudgement,name='getJudgement')
]
