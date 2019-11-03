from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.

def index(request):
	return render(request,"index.html")


def contact(request):
	if  request.method == 'POST':
		name=request.POST.get('name', '')
		city=request.POST.get('city','')
		country=request.POST.get('country','')
		subject=request.POST.get('subject','')
		
		contact = Contact(name=name, city=city,country=country,subject=subject)
		contact.save()
	return render(request, "contact.html")	

def success(request):
	return render(request,"success.html")


def cart(request):
	return render(request,"cart.html")



		
