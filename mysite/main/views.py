from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'main/home.html')

def test(request):
	return render(request, 'main/test.html')
