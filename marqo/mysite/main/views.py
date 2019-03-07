from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'main/home.html')

def purpose(request):
	return render(request, 'main/purpose.html')

def team(request):
	return render(request, 'main/team.html')

def contact(request):
	return render(request, 'main/contact.html')

def test(request):
	return render(request, 'main/test.html')
