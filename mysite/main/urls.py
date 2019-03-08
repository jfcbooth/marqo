from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('purpose/', views.purpose, name='purpose'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('coming-soon/', views.comingSoon, name='coming-soon'),
    path('test/', views.test, name='test'),
]
