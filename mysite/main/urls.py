"""mysite URL Configuration

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

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('earl48/', views.earl48, name='earl48'),
    path('earl46/', views.earl46, name='earl46'),
    path('earl44/', views.earl44, name='earl44'),
    path('orange229/', views.orange229, name='orange229'),
    path('burd326/', views.burd326, name='burd326'),
    path('burd328/', views.burd328, name='burd328'),
]
