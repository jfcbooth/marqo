from django.urls import path, include
from django.conf.urls import url
from main.views import HomeView
from . import views

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    path('purpose/', views.purpose, name='purpose'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('coming-soon/', views.comingSoon, name='coming-soon'),
    path('test/', views.test, name='test'),
    path('received/', views.received, name='received'),
]
