from django.shortcuts import render
from datetime import datetime
from .models import Burd326, Burd328, Orange229, Earl44, Earl46, Earl48
# Create your views here.

current_date = datetime.now()
formatted_date = current_date.strftime("%Y%m%d")

Burd326_data = Burd326.objects.all()
Burd328_data = Burd328.objects.all()
Orange229_data = Orange229.objects.all()
Earl44_data = Earl44.objects.all()
Earl46_data = Earl46.objects.all()
Earl48_data = Earl48.objects.all()
data = {'Burd326': Burd326_data,
		'Burd328': Burd328_data,
		'Orange229': Orange229_data,
		'Earl44': Earl44_data,
		'Earl46': Earl46_data,
		'Earl48': Earl48_data,
		'current_date': formatted_date
		}


def index(request):
	#Returns html page instead of raw html
	return render(request, 'main/home.html', context=data)

def earl48(request):
	#Returns html page instead of raw html
	return render(request, 'main/earl48.html', context=data)

def earl46(request):
	#Returns html page instead of raw html
	return render(request, 'main/earl46.html', context=data)

def earl44(request):
	#Returns html page instead of raw html
	return render(request, 'main/earl44.html', context=data)

def orange229(request):
	#Returns html page instead of raw html
	return render(request, 'main/orange229.html', context=data)

def burd326(request):
	#Returns html page instead of raw html
	return render(request, 'main/burd326.html', context=data)

def burd328(request):
	#Returns html page instead of raw html
	return render(request, 'main/burd328.html', context=data)


def test(request):
	#Returns html page instead of raw html
	return render(request, 'main/test.html', context=data)
